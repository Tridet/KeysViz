function barchart_left(elt, data, filter_count, w, h, var_color, alphabetical = false) {

    var keys = stroke2freq(data, filter_count, alphabetical = false)

    var val = []
    keys.forEach( function(d){
        val.push(d.value)
    });
    var max_percentage = d3.max(val);

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
    var yAxis = d3.axisRight(yScale);

    yScale.domain(strokeNames);
    xScale.domain([max_percentage,0]);

    xAxisG.call(xAxis)
    yAxisG.call(yAxis).attr("transform", "translate(" + w + " ,0)");

    elt.selectAll(".bar")
        .data(keys)
        .enter().append("rect")
        .attr("class", "bar")
        .attr("width", function(d) {return w-xScale(d.value); } )
        .attr("x", function(d) { return xScale(d.value); })
        .attr("y", function(d) { return yScale(d.key); })
        .attr("height", yScale.bandwidth())
        .style("fill", var_color)
        .on("mouseenter", function(d) {
            d3.select("svg").selectAll(".bar")
                .attr("opacity", function(e) {
                    return e.key===d.key ? 1: .1;
                })
            elt.append("text")
                .attr("id","label")
                .attr("x", xScale(d.value)-40)
                .attr("y", yScale(d.key)+13)
                .text(d.value.toFixed(2))
        })
        .on("mouseleave", function(d) {
            d3.select("svg").selectAll(".bar")
                .attr("opacity", 1)
            d3.selectAll("#label").remove()
        });

    // text label for the x axis
    elt.append("text")
        .attr("transform",
            "translate(" + (w/2) + " ," + (h*1.05) + ")")
        .style("text-anchor", "middle")
        .style("font-size", 14)
        .style("font-family", "monospace")
        .text("Percentage of total key strokes (%)");


    // text label for the y axis
    /*
    elt.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left*0.8)
        .attr("x",0 - (h / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .style("font-size", 14)
        .style("font-family", "monospace")
        .text("Keystroke");
     */
};
