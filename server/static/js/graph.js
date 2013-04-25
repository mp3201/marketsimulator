/**
 * 	Represents a time serie to be rendered on graph 
 * @param {Instance}    source 	 -- source object for the time serie
 * @param {map<int, list<(float, float)>>} data -- initial data to be rendered 
 */
function TimeSerie(source, initialData) {
	var self = source;
	
	self._data = ko.observable([]);
	
	/**
	 *	Should be the timeserie visible on a graph 
	 */
	self.visible = ko.observable(true);
	
	/**
	 *  Appends updates in the time serie 
 	 *  @param {list<(float, float)>} dataDelta -- list of pair (time, value) to be appended to the time serie
	 */
	self.appendData = function (dataDelta) {
		self._data(self._data().concat(dataDelta));
	}

	/**
	 *	Updates time serie from data fetched from server
	 *  @param {map<int, list<(float, float)>>} -- time serie relevant data fetched from server 
	 */	
	self.updateFrom = function (ts_changes) {
		if (ts_changes[self.uniqueId()]) {
			self.appendData(ts_changes[self.uniqueId()]);
		}
	}
	
	self._base_clone = source.clone;
	
	self.clone = function () {
		return TimeSerie(self._base_clone());
	}
	
	if (initialData) {
		self.updateFrom(initialData);
	}
	
	/**
	 *	Resets time serie data 
	 */
	self.resetData = function () {
		self._data([]);
	}
	
	/**
	 *	Returns time serie data to be rendered 
	 */
	self.getData = ko.computed(function () {
		return self._data();
	});
	
	/**
	 *	Returns true iff there is no data to render 
	 */
	self.empty = ko.computed(function () {
		return self._data().length == 0;
	});
	
	return self;
}

var makeTimeSerie = TimeSerie;

function firstChild(e) {
    for (var j=0; j<e.childNodes.length; j++) {
        if (e.childNodes[j].nodeType == 1) {
            return e.childNodes[j];
        }
    }    
    return undefined;
}

function Graph(source, root) {
	
	var self = source;
	
	/**
	 *	Returns an array of TimeSerie instances held by the graph 
	 */
	self.series = ko.computed(function () {
		var timeseries = source.fields()[0].impl().elements();
		return map(timeseries, function (timeserie) {
			return root.id2obj.lookup(timeserie.impl().pointee().uniqueId());
		});
	});
		
	self.asFlotr = ko.computed(function () {
		var dummy = root.updategraph();
		console.log("asFlotr for " + self.alias());
		return map(self.series(), function (ts) {
			return ts.visible() ? { 
				'source' : ts,
				'data' : ts.getData.peek(), 
				'label' : ts.alias.peek(), 
				'name': ts.alias.peek() 
			} : {};
		});		
	})
	
	self.empty = ko.computed(function () {
		return all(self.series(), function (timeserie) {
			return timeserie.empty();
		});
	});
	
	self._base_clone = source.clone;
	
	self.clone = function () {
		return Graph(self._base_clone(), root);
	}
	
	return self;
}

var makeGraph = Graph;

function viewport()
{
	var e = window
	  , a = 'inner';
	if ( !( 'innerWidth' in window ) )
	{
		a = 'client';
		e = document.documentElement || document.body;
	}
	return { width : e[ a+'Width' ] , height : e[ a+'Height' ] }
}

ko.bindingHandlers.flotr = {
    update:function (element, valueAccessor, allBindingsAccessor, viewModel) {
    	
		var data = ko.utils.unwrapObservable(valueAccessor());
		var metrics = viewport();
        
        element.style.width = Math.round(metrics.width*0.89)+'px';
        element.style.height = Math.round(metrics.height*0.9)+'px';
        
        Flotr.draw(element, data, {
            legend : {
                position : 'se',            // Position the legend 'south-east'.
                backgroundColor : '#D2E8FF' // A light blue background color.
            },
            HtmlText : false
        });
    }
}

ko.bindingHandlers.highstocks = {
    update:function (element, valueAccessor, allBindingsAccessor, viewModel) {
    	
		var data = ko.utils.unwrapObservable(valueAccessor());

        new Highcharts.StockChart({
        	chart: {
        		renderTo: element.id,
        		type: 'line',
        		animation: false
        	},
        	series: data,
		    rangeSelector: {
		    	enabled: false
		    },	        
	        xAxis: {        
	            labels: {
	                format: '{value}'
	            }
	        },
	        legend: {
	        	enabled: true
	        }, 
	        credits: {
	        	enabled: false
	        },
	        plotOptions: {
	            series: {
                	animation: false
            	},
            	line: {
	        		dataGrouping: {
	        			groupPixelWidth: 2,
	        			approximation: "open"
	        		}
	        	}
	        }	        	
        });
    }
}