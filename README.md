# volga
A python and js/html tool for storing, comparing, and nicely presenting news wires. Before I finish this md, see [here](https://mittmattmutt.medium.com/an-os-tool-for-storing-searching-and-displaying-news-wires-b9c81dbbbe3a)  for more information.

__I recommend not using this at the moment--the same functionality can be achieved much easier by i) ditching all the python stuff (the reader isn't necessary because Telegram lets you download in JSON, the lemmatizer isn't neccessary because arguably the most important words are names it struggles with); ii) expanding the js graphing to include comparisions and iii) using the HTML5 file api to let users send data to an app that does everything client side, making this essentially no-code thus way more user friendly. I'll change it in the next couple of days__ 

# Necessities
You'll need python and all the libraries in volga.py

More importantly, you'll need to do the below, having i) downloaded and ii) read and lemmatized whatever sets of stories you want. 
# Thing 1
* You will have a lemmatized and a plain version of your stories.
* Copy them to the directory of the html. Open the lemmatized one in text editor, and add ```var telegram_lemmatized=``` before the dict, so the text reads something like:

```var telegram_lemmatized={"01.03.2022 01:13:1": "правительство Япония утвердить введение санкция против шести представитель руководство Россия , включая президент Владимира Путин ...```

* Then rename the file with a .js extension.

* Open the raw one, and add "var telegram_raw=" before the dict, and similarly rename.

* In so doing, you've turned the output of the python script into something the html file can read.

* Next, and finally, open index.html in a text editor, find this bit:

```<title>Volga</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="513_lemmatized_ua.js"></script>
<script src="513_raw_ua.js"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
```

* And change the last two <script src>'s so that they point towards the .js's you made above.

# Thing 2
  * In a rush to finish this, I didn't end up implementing in the html a way to autogenerate the x-axis. So you need to enter it manually. Go to l155, which reads
  ```const labels = Array.from({length : 37}, (_, v) => v+1)```
  
  And change 37 to how many days coverage you have.
  
