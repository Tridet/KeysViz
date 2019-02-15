function stroke2freq(data, filter_count, alphabetical = false) {

        var keys = d3.nest()
            .key(function (d) {
                return d["stroke"];
            })
            .rollup(function (v) {
                return v.length;
            })
            .entries(data);

        //var keys = keys.filter(d => d.value > filter_count);

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
