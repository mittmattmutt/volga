import simplemma
import codecs
import json

def write(inn, out):
#this takes an input file of the form message[n].html and returns a dict-ified version of it
#the keys of which are the date stamps of the messages
#isnt' called directly by user but can be

    f=open(inn, encoding="utf-8")

    text=f.read()

    stories={}
    time_location=0

    found=False

    while found==False:
        time_location=text.find('"pull_right date details" title="', time_location)
        if(time_location==-1):
            found=True
        #print(time_location)
        time_location=time_location+33
        end_time=time_location+18
        #print(end_time)
        date=text[time_location: end_time]
        #print(date)
        
        story_location=text.find('t">', end_time)
        story_end=text.find('</div',story_location)
        story=text[story_location+4: story_end]
        stories[date]=story
        #print(stories[date])
        time_location=story_end
        #print(stories[date])



    with codecs.open(out, 'w', encoding="utf-8") as convert_file:
                  convert_file.write(json.dumps(stories, ensure_ascii=False))

    return(stories)

def read(file):
    f=open(file, encoding="utf-8")
    text=f.read()
    stories=json.loads(text)
    return stories
#shouldn't be needed. auxiliary to read files of parsed stories

def lemmatize(story_dict, out, lang):
    langdata=simplemma.load_data(lang)
#this takes a dict and writes a lemmatized version of that dict to file
    new_dict={}
    count=0
    
    #listed_stories=list(story_dict)
    for x in story_dict: 
        count=count+1
       # if count==4:
        #    break;
        print("Lemmatizing "+str(count)+" of 992")
        print(x)
        #lemma_array=[]
        lemmas=simplemma.text_lemmatizer(story_dict[x], langdata)
        new_dict[x]=' '.join(lemmas)
        

    
    with codecs.open(out, 'w', encoding="utf-8") as convert_file:
            convert_file.write(json.dumps(new_dict, ensure_ascii=False))

def batchwrite(in_files, out_files, output_file):
    z={}
    count=0
#this write in batches; you have to specify the names of the in and out files in arrays
    for file in in_files:
        z.update(write(file,out_files[count]))
        count=count+1
        
    with codecs.open(output_file, 'w', encoding="utf-8") as convert_file:
                      convert_file.write(json.dumps(z, ensure_ascii=False))
    return z
    
###the above are the main text processing routines: they take what Telegram gives
##and produce something computers and read and you can search


    
