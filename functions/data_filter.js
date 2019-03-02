function data_filter(data, main_key, filter_count, alphabetical = false) {

    var dict = data[main_key];
    var keys = [];

    for (var k in dict){
        keys.push({value : dict[k], key : k});
    };

    var sum_keys = d3.sum(keys, function (d) {
        return d.value;
    });

    keys.forEach(function (d) {
        d.value = d.value / sum_keys * 100;
    });

    keys.sort(function (x, y) {
        return d3.ascending(x.value, y.value);
    });

    if (alphabetical===false){
        var keys = keys.slice(keys.length - filter_count);
    }
    
    if (alphabetical === true) {
        alph = "abcdefghijklmnopqrstuvwxyz" //je connais mon alphabet
        keys.sort(function (x, y) {
            return d3.descending(x.key, y.key)
        });

        // on filtre pour ne garder que les lettres
        keys = keys.filter(function(x){
            if (/[a-z]{1}/.test(x.key) && x.key.length==1){
                return x;
            }
        })

        //on ajoute les lettres manquantes
        for (var k=0; k<26; k++){
            if (!(alph[25-k] == keys[k].key)){
                keys.splice(k, 0, {value : 0, key : alph[25-k]})
            }
        }
    };

    return keys;
}

function transform_data(data) {

    var transform_data_dict = {};
    for (var main_key in data){
        var dict = data[main_key];
        var keys = [];
        for (var k in dict){
            keys.push({value : dict[k], key : k});
        };
        var sum_keys = d3.sum(keys, function (d) {
            return d.value;
        });

        keys.forEach(function (d) {
            d.value = d.value / sum_keys //* 100;
        });

        var keys_dict = {}
        keys.forEach(function(d){
            keys_dict[d.key] = d.value;
        });

        transform_data_dict[main_key] = keys_dict
    };
    return transform_data_dict;
}