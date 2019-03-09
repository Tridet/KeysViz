# KeysViz Project

This repository hosts the KeysViz project motivated by the 
[interactive data visualization class](https://github.com/LyonDataViz/MOS5.5-Dataviz) given by 
[Romain Vuillemot](https://github.com/romsson), during my last year at École Centrale de Lyon.

## Record your own keystrokes and analyze it

This project aims at creating different D3js visualizations showing insights from personal keyboard strokes data. 
For this purpose a keylogger has been implemented.

The project is available [here](https://tridet.github.io/KeysViz/index.html) and use our personal logs while doing 
different actions such as writing e-mails or coding in D3.js. We also use 'Les Miserables' and 'The Orient Express' 
books for a basis of comparison.

**For a better user experience use the website with Google Chrome browser!**

## Try it

You can also use the website with your own personal data.

### 1. Install the keylogger and record keystrokes

You can choose to launch and stop the keylogger at anytime hence avoiding to record sensitive personal 
data such as passwords. To use the keylogger inside the keylogger folder use the README.md file inside it.

### 2. Load your personal logs

Once you've recorded your personal keystrokes you can put your logs inside the data/logs folder and 
remove all the files (.txt or .csv) not dealing with 'miserables' or 'christie' (unless you do not want to use it). 
The logs must be named according to their categories and must be unique, for example 'mail.txt' for logs about e-mails.

### 3. Parse the data

Run python function 'run.py' to parse your data.


### 4. Change the path name to use within the HTML pages

In order to use your personal data on the website you need to do some modifications :

Within the pages keyboard_viz and barchart_viz you will have to change the variable **data_path**.

Within the page chords_viz you will have to change the variable **filename**.

You will also have to change the value inside the dropdown menus and the legend dictionaries inside these three pages.

### 5. Visualize the insights
The data we created with our own keylogger were interesting, but we added texts from famous authors to compare 
the characters used. Hence, there are some data we can't access (like, how many times "backspace" was used in some texts).

**1. Keyboard**
* The [keyboard visualization](https://tridet.github.io/KeysViz/keyboard_viz.html) allows us to see the keys 
most frequently typed by the user in different contexts. The intensity shows what key was striked the most. 
Obviously, "e" and "space" are typed a lot, but we realized that "backspace" is often the most used key 
(when we have information about it being typed). When they hover on a key with the mouse, users can see a 
detailed radar graph that breaks down the use of that particular key in all datasets. 
    
<div>
<img src="assets/images/demo-viz1.gif">
</div>

   * Some insights : 
        * There are a lot of spaces and backspaces
        * All keyboard is used when coding which is not the case when
        writing e-mails or philosophy paper
        * Loic always uses shift right instead of Pascal and Theo who
        use shift left
        * The letter 'e' is more used when dealing with literary 
        categories
        * Some letters are more used in English than in French and vice versa
    

**2.  Barcharts**

* The [barcharts visualization](https://tridet.github.io/KeysViz/barchart_viz.html) shows us a ranking of which 
characters were the most used. Hovering on a bar highlights the bar corresponding to the same character on the 
other chart. Users can change which texts they want to compare, and if they want to see a ranking by frequency 
or the characters in alphabetical order (in this case, we kept only the letters and discarded special characters).

<div>
<img src="assets/images/demo-viz2.gif">
</div>

   * Some insights :
       * Backspace is the most used keystroke
       * There are a lot of non alphanumeric characters while coding :
       frequency of letters are twice as low 
       * There are more 'v' and 'd' letters for D3 than for Matlab : the
       names 'var' and 'd3' are used a lot. There are more parenthesis, 
       i.e. characters '(' and ')', for Matlab than for D3 : they are 
       used a lot for mathematic operations and in matrices.
       * Even if we had very few data for the category 'mail' the
       distribution of the letters are very similar to those used in the
       book 'Les Miserables' from Victor Hugo
       * When you compare the two books from Agatha Christie and Victor 
       Hugo you can see that the global distribution are quite the same :
       Latin root language. However we can see that some letters are more 
       used in french such as 'e', 'q' and 'u' and vice versa such as 'g', 
       'h', 'k', 'w' and 'y'.
       * The occurences of spaces and dots  allow you to count the average
       letters by word and the average words by sentence. Hence you can see 
       that there are on average 5 letters by word in both languages and that 
       sentences in English are on average smaller than in French.

**3. Chords diagram**

* The [chord diagram visualization](https://tridet.github.io/KeysViz/chords_viz.html) is certainly the most complex 
graph we made : it shows what characters are most likely to follow each character. We had to filter the data in order 
to keep the graph readable and to avoid information overload. The insight is not obvious at first sight, but one can 
guess that the five vowels represents a little less than half of all the letters typed. Also, mouseover a character 
highlights the links between it and the other characters, and mouseover a link highlights it.

<div>
<img src="assets/images/demo-viz3.gif">
</div>

   * Some insights :
       * About half of the letters typed are vowels - which is reasonable.
       * It is quite easy to follow the chords to form words : for instance, if you take a french text, "l" is most often followed by "e" and "a", indicating the words "le" and "la" are very common. In fact, you can spend quite some time trying to find this kind of things, following the chords.
       * In english texts, you can see "h" follows "t" and then "e" follows "h" most often, which corresponds to "the".
       * A letter that follows itself shows a chord that collapses onto itself. Representation could indeed be improved in this regard.
       * For readability purposes, some letters don't have any chord attached, because it would be too thin (it is the case for "k", "x" and "z" for instance).

## Authors

* Loïc BETHENCOURT
* Pascal GODBILLOT 
* Théo LACOUR

## Credits

* The radar chart visualisation is inspired by the following [block buider](http://bl.ocks.org/nbremer/21746a9668ffdf6d8242).
* The chords diagram visualisation is inspired by the following [gist](https://gist.github.com/sghall/7859113).
* The website is inspired by the following [HTML template](http://www.mashup-template.com/preview.html?template=univers).
