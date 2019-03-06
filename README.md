# KeysViz Project

This repository hosts the KeysViz project motivated by the [interactive data visualization class](https://github.com/LyonDataViz/MOS5.5-Dataviz) given by [Romain Vuillemot](https://github.com/romsson), during my last year at École Centrale de Lyon.

## Record your own keystrokes and analyze it

This project aims at creating different D3js visualizations showing insights from personal keyboard strokes data. For this purpose a keylogger has been implemented.

The project is available [here](https://tridet.github.io/KeysViz/index.html) and use our personal logs while doing different actions such as writing e-mails or coding in D3.js. We also use 'Les Miserables' and 'The Orient Express' books for a basis of comparison.

## Try it

You can also use the website with your own personal data.

### 1. Install the keylogger and record keystrokes

You can choose to launch and stop the keylogger at anytime hence avoiding to record sensitive personal data such as passwords. To use the keylogger inside the keylogger folder use the README.md file inside it.

### 2. Load your personal logs

Once you've recorded your personal keystrokes you can put your logs inside the data/logs folder and remove all the files (.txt or .csv) not dealing with 'miserables' or 'christie' (unless you do not want to use it). The logs must be named according to their categories and must be unique, for example 'mail.txt' for logs about e-mails.

### 3. Parse the data

Run python function 'run.py' to parse your data.


### 4. Change the path name to use within the HTML pages

Within the pages keyboard_viz and barchart_viz you will have to change the variable **data_path**.

Within the page chords_viz you will have to change the variable **filename**.

You will also have to change the value inside the dropdown menus and the legend dictionary inside these three pages.

### 5. Visualize the insights
The data we created with our own keylogger were interesting, but we added texts from famous authors to compare the characters used. Hence, there are some data we can't access (like, how many times "backspace" was used in some texts).

The [keyboard visualization](https://tridet.github.io/KeysViz/keyboard_viz.html) allows us to see the keys most frequently typed by the user in different contexts. The intensity shows what key was striked the most. Obviously, "e" and "space" are typed a lot, but we realized that "backspace" is often the most used key (when we have information about it being typed). When they hover on a key with the mouse, users can see a detailed radar graph that breaks down the use of that particular key in all datasets.

<div>
<img src="assets/images/demo-viz1.gif">
</div>

The [barcharts visualization](https://tridet.github.io/KeysViz/barchart_viz.html) shows us a ranking of which characters were the most used. Hovering on a bar highlights the bar corresponding to the same character on the other chart. Users can change which texts they want to compare, and if they want to see a ranking by frequency or the characters in alphabetical order (in this case, we kept only the letters and discarded special characters).

<div>
<img src="assets/images/demo-viz2.gif">
</div>

The [chord diagram visualization](https://tridet.github.io/KeysViz/chords_viz.html) is certainly the most complex graph we made : it shows what characters are most likely to follow each character. We had to filter the data in order to keep the graph readable and to avoid information overload. The insight is not obvious at first sight, but one can guess that the five vowels represents a little less than half of all the letters typed. Also, mouseover a character highlights the links between it and the other characters, and mouseover a link highlights it.

<div>
<img src="assets/images/demo-viz3.gif">
</div>


## Authors

* Loïc BETHENCOURT
* Pascal GODBILLOT 
* Théo LACOUR

## Credits

* The radar chart visualisation is inspired by the following [block buider](http://bl.ocks.org/nbremer/21746a9668ffdf6d8242)
