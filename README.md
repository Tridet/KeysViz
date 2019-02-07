# KeysViz Project

This repository hosts the KeyViz project motivated by the [interactive data visualization class](https://github.com/LyonDataViz/MOS5.5-Dataviz) given by [Romain Vuillemot](https://github.com/romsson), during my last year at École Centrale de Lyon.

The project is available [here](https://tridet.github.io/KeysViz/index.html).

This project aims at creating different D3js visualizations showing personal keyboard strokes data. For this purpose a keylogger has been implemented.

Authors : Loïc BETHENCOURT - Pascal GODBILLOT - Théo LACOUR

<!DOCTYPE html>
<head>
  <meta charset="utf-8">
  <script src="https://d3js.org/d3.v4.min.js"></script>
  <style>
    body { margin:0;position:fixed;top:0;right:0;bottom:0;left:0; }
  </style>
</head>
<body>
  
<script>
  
  //Define the global variables
  var outerWidth = 900;
  var outerHeight = 530
	var margin = {top: 30, right:80, bottom:80, left: 150};
  
  var innerWidth = outerWidth - margin.left - margin.right;
  var innerHeight = outerHeight - margin.top - margin.bottom;
  
  
  //Create the SVG
  var svg = d3.select("body").append("svg")
  .attr("width", outerWidth)
  .attr("height", outerHeight);
        
  var g = svg.append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
  var xAxisG = g.append("g")
  .attr("class", "x_axis")
  .attr("transform", "translate(0,"+ innerHeight +")")
  .style("font-family", "monospace")
  .style("font-size", 12)
  
   var yAxisG = g.append("g")
  .attr("class", "y_axis")
  .style("font-family", "monospace")
  .style("font-size", 12);
    
  var yScale = d3.scaleBand()
  .paddingInner(0.07)
  .range([innerHeight,0]);
  
  var xScale = d3.scaleLinear()
  .range([0,innerWidth]);
  
  var colorScale = d3.scaleOrdinal()
  
  var xAxis = d3.axisBottom(xScale);
  var yAxis = d3.axisLeft(yScale)//.tickFormat(d3.format(".2s")) ;
  var parseDate = d3.timeParse("%Y-%m-%d %H:%M:%S,%L");
  var displayDate = d3.timeFormat("%Y-%m-%d %H:%M:%S,%L");
  //     console.log(parseDate("2019-01-29 10:28:05,248"));
  var data_link = "https://raw.githubusercontent.com/Tridet/KeysViz/master/data/pascal/logs_js.txt"
	
  d3.text(data_link, function(error, raw){
    var dsv = d3.dsvFormat(';')
    var data = dsv.parse(raw)
    data.forEach(function(d) {
      d["stroke"] = d["stroke"].toString();
      d["date"] = parseDate(d["date"]);
    });
    
    var keys = d3.nest()
    .key(function(d) { return d["stroke"]; })
    .rollup(function(v) { return v.length; })
    .entries(data);
    
    var keys = keys.filter(d => d.value > 7);
    keys.sort(function(x, y){
      return d3.descending(x.value, y.value)});
    
    var sum_keys = 0
    keys.forEach(function(d) {
      sum_keys+=d.value
    });
    
    keys.forEach(function(d) {
      d.value=d.value/sum_keys*100
    });
    
    var max_percentage = keys[0].value
    
    var strokeAccessor = function(d) {
      return d.key
    };
    var strokeNames = d3.set(keys.map(strokeAccessor)).values(); 
    yScale.domain(strokeNames);
    
    console.log(yScale)
      
    xScale.domain([0, max_percentage]);
  
    xAxisG.call(xAxis)
    yAxisG.call(yAxis);
    
    // append the rectangles for the bar chart
    g.selectAll(".bar")
      .data(keys)
      .enter().append("rect")
      .attr("class", "bar")
    //.attr("x", function(d) { return xScale(d.value); })
      .attr("width", function(d) {return xScale(d.value); } )
      .attr("y", function(d) { return yScale(d.key); })
      .attr("height", yScale.bandwidth())
    	.style("fill", "salmon");
    // text label for the x axis
    g.append("text")             
      .attr("transform",
            "translate(" + (innerWidth/2) + " ," + (innerHeight + 1.2*margin.top) + ")")
      .style("text-anchor", "middle")
      .style("font-size", 14)
      .style("font-family", "monospace")
      .text("Percentage of total key strokes (%)");
    // text label for the y axis
    g.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left*0.6)
      .attr("x",0 - (innerHeight / 2))
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .style("font-size", 14)
      .style("font-family", "monospace")
      .text("Keystroke");  
    // title of the ligne chart
    g.append("text")             
      .attr("transform",
            "translate(" + (innerWidth/2) + " ," + (-margin.top*0.1) + ")")
      .style("text-anchor", "middle")
      .style("font-size", 16)
      .style("font-family", "monospace")
      .text("Bar chart of key strokes while coding in D3.js");
    
        
   
    });
  
</script>
 
</body>
