import syntax.scala.Printer.{typed => pp}
import predef.ScPrintable
import shapeless.syntax.typeable._
import scala.collection.immutable._
import Typed.AfterTyping

package object NameTable {

    class Scope(val name : String = "_root_") extends pp.NamesScope with ScPrintable {

        var packages = Map[String, Scope]()
        var anonymous = List[Scope]()
        var members = Map[String, AST.Member]()
        var attributes = Typed.Attributes(Map.empty)
        var parent : Option[Scope] = None
        var typed : Option[Typed.Package] = None

        val isRoot = name == "_root_"

        def add(m : AST.Member) {
            check_name_is_unique(m.name, m)
            members = members updated (m.name, m)
        }

        def qualifyName(x : String) : AST.QualifiedName =
            AST.QualifiedName(qualifiedName.names :+ x)

        def qualifiedName : AST.QualifiedName =
            AST.QualifiedName(
                if (isRoot)
                    "" :: Nil
                else
                    parent.get.qualifiedName.names :+ name
            )


        override def equals(o : Any) = true

        private def check_name_is_unique(name : String, e : Any) {
            if (members contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + members(name) + "\r\n" + e)
            if (packages contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + packages(name) + "\r\n" + e)
            anonymous foreach { _.check_name_is_unique(name, e) }
        }

        def add(a : AST.Attribute) {
            attributes.items get a.name match {
                case None => attributes = Typed.Attributes(attributes.items updated (a.name, a.value))
                case Some(v) =>
                    throw new Exception(s"Duplicate definition for package attribute ${qualifyName(a.name)}: $v => ${a.value}" )
            }
        }

        def add(p : AST.PackageDef) {
            def populate(src: Scope, child: Scope) = {
                if (members contains child.name)
                    throw new Exception(s"Duplicate definition for ${child.name}:\r\n" + members(child.name) + "\r\n" + child)
                if (!(packages contains child.name)) {
                    src.packages = src.packages updated(child.name, child)
                    child.parent = Some(src)
                }
                src.packages(child.name)
            }
            val target = p.name match {
                case Some(qn) =>
                    (qn.names map (new Scope(_))).foldLeft(this) { populate }
                case None =>
                    val fresh = new Scope("$" + anonymous.length)
                    anonymous = fresh :: anonymous
                    fresh.parent = Some(this)
                    fresh
            }
            create(p.members, p.attributes, target)
        }

        def getPackageOrCreate(name : String) =
            packages get name match {
                case Some(p) => p
                case None    =>
                    val p = new Scope(name)
                    p.parent = Some(this)
                    packages = packages updated (name, p)
                    p
            }

        def lookup[T <: AST.Member](qn : List[String], visited : HashSet[Scope] = HashSet.empty)(implicit t : Manifest[T]) : Option[(Scope, T)] = {
            if (visited contains this)
                None
            else {
                val v = visited + this
                qn match {
                    case Nil => throw new Exception("Qualified name cannot be empty")
                    case "" :: tl =>
                        if (isRoot)
                            lookup(tl)
                        else
                            parent.get lookup (qn,v)
                    case _ =>
                        anonymous map { _ lookup (qn, v) } find { _.nonEmpty } match {
                            case Some(Some((scope, x))) => Some((scope, x.asInstanceOf[T]))
                            case Some(None) => throw new Exception("cannot occur")
                            case None =>
                                qn match {
                                    case x :: Nil =>
                                        members get x match {
                                            case Some(f) if f.cast[T].nonEmpty => Some((this, f.asInstanceOf[T]))
                                            case _ => parent flatMap { _ lookup (qn, v) }
                                        }
                                    case x :: tl =>
                                        packages get x map { _ lookup tl } match {
                                            case None => parent flatMap { _ lookup (qn, v) }
                                            case y => y.get
                                        }
                                }
                        }
                }
            }
        }

        def lookupFunction(name : List[String]) : Option[(Scope, AST.FunDef)] = lookup[AST.FunDef](name)
        def lookupFunctionAlias(name : List[String]) : Option[(Scope, AST.FunAlias)] = lookup[AST.FunAlias](name)
        def lookupType(name : List[String]) : Option[(Scope, AST.TypeDeclaration)] = lookup[AST.TypeDeclaration](name)

        def resolveFunction(name : AST.QualifiedName) : Option[(Scope, AST.FunDef)] =
            lookupFunction(name.names) match {
                case r : Some[_] => r
                case None =>
                    lookupFunctionAlias(name.names) match {
                        case Some((scope, alias)) =>
                            scope resolveFunction alias.target
                        case None =>
                            None
                    }
            }

        def toTyped(target : Typed.Package) : Typed.Package =
        {
            typed = Some(target)
            packages.values foreach {
                p => p.toTyped(target.createChild(p.name, p.attributes))
            }
            anonymous foreach {
                p => p.toTyped(target.createChild(p.attributes))
            }
            target
        }
    }

    private def create(p : AST.Definitions, a : Iterable[AST.Attribute], impl : Scope) {
        p.definitions foreach {
            case m : AST.Member => impl.add(m)
            case package_def : AST.PackageDef => impl.add(package_def)
        }
        a foreach { impl.add }
    }



    def apply(p : List[AST.Definitions]) : Scope =
    {
        val impl : Scope = new Scope

        p foreach { create(_, Nil, impl) }

        Typed.BeforeTyping(impl)

        impl
    }

}
