function stroke2dict(data, filter_count, alphabetical = false) {
    dict = {}
    var keys = stroke2freq(data, filter_count, alphabetical = false)
    keys.forEach(function(d){
       dict[d.key] =  d.value/100
    });
    return dict;
};