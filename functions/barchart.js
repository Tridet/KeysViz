function barchart(elt, data, filter_count, w, h, var_color) {

  var keys = d3.nest()
  .key(function(d) { return d["stroke"]; })
  .rollup(function(v) { return v.length; })
  .entries(data);

  var keys = keys.filter(d => d.value > filter_count);

  keys.sort(function(x, y){
    return d3.descending(x.value, y.value)});

  var sum_keys = d3.sum(keys, function(d){ return d.value; });

  keys.forEach(function(d) {
    d.value=d.value/sum_keys*100
  });

  var max_percentage = keys[0].value;

  var strokeAccessor = function(d) {
    return d.key
  };

  var strokeNames = d3.set(keys.map(strokeAccessor)).values();

  var xAxisG = elt.append("g")
  .attr("class", "x_axis")
  .attr("transform", "translate(0,"+ h +")")
  .style("font-family", "monospace")
  .style("font-size", 12)

  var yAxisG = elt.append("g")
  .attr("class", "y_axis")
  .style("font-family", "monospace")
  .style("font-size", 12);

  var yScale = d3.scaleBand()
  .paddingInner(0.07)
  .range([h,0]);

  var xScale = d3.scaleLinear()
  .range([0,w]);

  var colorScale = d3.scaleOrdinal()

  var xAxis = d3.axisBottom(xScale);
  var yAxis = d3.axisLeft(yScale);

  yScale.domain(strokeNames);  
  xScale.domain([0, max_percentage]);

  xAxisG.call(xAxis)
  yAxisG.call(yAxis);

  elt.selectAll(".bar")
    .data(keys)
    .enter().append("rect")
    .attr("class", "bar")
    .attr("width", function(d) {return xScale(d.value); } )
    .attr("y", function(d) { return yScale(d.key); })
    .attr("height", yScale.bandwidth())
    .style("fill", var_color);

  // text label for the x axis
  elt.append("text")             
    .attr("transform",
          "translate(" + (w/2) + " ," + (h + 1.3*margin.top) + ")")
    .style("text-anchor", "middle")
    .style("font-size", 14)
    .style("font-family", "monospace")
    .text("Percentage of total key strokes (%)");


  // text label for the y axis
  elt.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - 0.8*margin.left)
    .attr("x",0 - (h / 2))
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .style("font-size", 14)
    .style("font-family", "monospace")
    .text("Keystroke");  
};
