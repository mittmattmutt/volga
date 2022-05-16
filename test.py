import volga

z={}
files=["messages.html", "messages2.html","messages3.html","messages4.html","messages5.html","messages6.html","messages7.html","messages8.html"]
files2=["m.txt", "m2.txt","m3.txt","m4.txt","m5.txt","m6.txt","m7.txt","m8.txt"]

volga.lemmatize(volga.batchwrite(files, files2, "513_raw_ua.txt"), "513_lemmatized_ua.txt", 'uk')

                
