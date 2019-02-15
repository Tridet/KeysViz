function filter_data(data, main_key, filter_count, alphabetical = false) {

    var dict = data[main_key]
    var keys = []

    for (var k in dict){
        keys.push({value : dict[k], key : k})
    }

    keys.sort(function (x, y) {
        return d3.ascending(x.value, y.value)
    });

    var keys = keys.slice(keys.length - filter_count);

    if (alphabetical === true) {
        keys.sort(function (x, y) {
            return d3.descending(x.key, y.key)
        });
    };

    var sum_keys = d3.sum(keys, function (d) {
        return d.value;
    });

    keys.forEach(function (d) {
        d.value = d.value / sum_keys * 100
    });

    return keys;
};
