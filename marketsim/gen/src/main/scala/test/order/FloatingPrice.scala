package test.order

import marketsim._
import marketsim.order
import marketsim.Scheduler._
import test._

case object FloatingPrice extends Test {

    def apply(trace_ : String => Unit)
    {
        def trace(s : String) = trace_(f"$currentTime%2.1f\t$s%s")

        marketsim.Scheduler.create { scheduler =>

            val local = new marketsim.orderbook.Local
            val link = new marketsim.orderbook.remote.TwoWayLink(() => 0.2, () => 0.3)
            val book = withLogging(trace)(new marketsim.orderbook.remote.Book(local, link))

            val A = new LoggedAccount(trace, book, "A")
            val B = new LoggedAccount(trace, book, "B")

            val sellOrders = LimitOrderFactory(() => 100 + currentTime.toInt, const(11))

            case class BuyPrices() extends (() => Option[Ticks])
            {
                def apply() = Some(95 + currentTime.toInt)
                override def toString() = apply().toString
            }

            val buyOrders_1 =
                    order.Iceberg.Factory(
                        order.FloatingPrice.Factory(
                            LimitOrderFactory(price = const(10) , volume = const(-25)),
                            OnEveryDt(1, BuyPrices())),
                        const(3)
                    )

            val buyOrders_2 =
                    order.FloatingPrice.Factory(
                        order.Iceberg.Factory(
                            LimitOrderFactory(price = const(10) , volume = const(-25)),
                            const(3)),
                        OnEveryDt(1, BuyPrices()))

            100 to 105 foreach { i => A.account send order.StopLoss.Order(MarketOrder(-1), i) }

            0 to 4 foreach { i => schedule(i,     A sendOrder sellOrders) }
            schedule(5, B sendOrder buyOrders_1)
            schedule(5, B sendOrder buyOrders_2)

            schedule(20, {
                A.ordersSent.getOrders foreach A.cancel
                B.ordersSent.getOrders foreach B.cancel
            })

            scheduler workTill 50
        }
    }
}