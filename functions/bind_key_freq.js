function getfreq (freq, key) {
	var frequency;
	if (freq[key] == undefined) {
		frequency = 0;
	}
	else {
		frequency = freq[key];
	}
	return frequency;
}

function binding (keyboard, freq) {
	keyboard.forEach(function(d,i) {
		var key = d.v;
		for (var cat in freq) {
			switch (key) {
				case '5':
					keyboard[i][cat] = getfreq(freq[cat], '(') + getfreq(freq[cat], key) ;
					break;
				case '°':
					keyboard[i][cat] = getfreq(freq[cat], key) + getfreq(freq[cat], ')');
					break;
				case '_':
					keyboard[i][cat] = getfreq(freq[cat], '-');
					break;
				case 'shift_L':
					keyboard[i][cat] = getfreq(freq[cat], 'shift');
					break;
				case 'shift_R':
					keyboard[i][cat] = getfreq(freq[cat], 'shift_r');
					break;
				case 'alt_L':
					keyboard[i][cat] = getfreq(freq[cat], 'alt');
					break;
				case 'alt_R':
					keyboard[i][cat] = getfreq(freq[cat], 'alt_r');
					break;
				case 'cmd_L':
					keyboard[i][cat] = getfreq(freq[cat], 'cmd');
					break;
				case 'cmd_R':
					keyboard[i][cat] = getfreq(freq[cat], 'cmd_r');
					break;
				case '$':
					keyboard[i][cat] = getfreq(freq[cat], '$') + getfreq(freq[cat], '*');
					break;
				case '=':
					keyboard[i][cat] = getfreq(freq[cat], '+') + getfreq(freq[cat], key);
					break;
				case ':':
					keyboard[i][cat] = getfreq(freq[cat], '/') + getfreq(freq[cat], key);
					break;
				case ';':
					keyboard[i][cat] = getfreq(freq[cat], '.') + getfreq(freq[cat], key);
					break;
				case ',':
					keyboard[i][cat] = getfreq(freq[cat], '?') + getfreq(freq[cat], key);
					break;
				default:
					keyboard[i][cat] = getfreq(freq[cat], key) + getfreq(freq[cat], key.toLowerCase());
			}
		}
	})
}