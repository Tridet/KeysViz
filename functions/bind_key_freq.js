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
		switch (key) {
			case '5':
				keyboard[i]["freq"] = getfreq(freq, '(') + getfreq(freq, key) ;
				break;
			case '°':
				keyboard[i]["freq"] = getfreq(freq, key) + getfreq(freq, ')');
				break;
			case '_':
				keyboard[i]["freq"] = getfreq(freq, '-');
				break;
			case 'shift_L':
				keyboard[i]["freq"] = getfreq(freq, 'shift');
				break;
			case 'shift_R':
				keyboard[i]["freq"] = getfreq(freq, 'shift_r');
				break;
			case 'alt_L':
				keyboard[i]["freq"] = getfreq(freq, 'alt');
				break;
			case 'alt_R':
				keyboard[i]["freq"] = getfreq(freq, 'alt_r');
				break;
			case 'cmd_L':
				keyboard[i]["freq"] = getfreq(freq, 'cmd');
				break;
			case 'cmd_R':
				keyboard[i]["freq"] = getfreq(freq, 'cmd_r');
				break;
			case '$':
				keyboard[i]["freq"] = getfreq(freq, '$') + getfreq(freq, '*');
				break;
			case '=':
				keyboard[i]["freq"] = getfreq(freq, '+') + getfreq(freq, key);
				break;
			case ':':
				keyboard[i]["freq"] = getfreq(freq, '/') + getfreq(freq, key);
				break;
			case ';':
				keyboard[i]["freq"] = getfreq(freq, '.') + getfreq(freq, key);
				break;
			case ',':
				keyboard[i]["freq"] = getfreq(freq, '?') + getfreq(freq, key);
				break;
			default:
				keyboard[i]["freq"] = getfreq(freq, key) + getfreq(freq, key.toLowerCase());
		}
	})
}