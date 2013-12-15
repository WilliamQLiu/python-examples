#nltk.download() # Test if NLTK was downloaded and installed correctly
import os # for path
import matplotlib #for dispersion plot
import numpy #for disperson plot
import nltk # for language processing

#Get number of syllables
#import curses
#from curses.ascii import isdigit 
#from nltk.corpus import cmudict
#d = cmudict.dict() 
def load_file(mypath):
	#book3 = open(os.path.expanduser("~/GitHub/Python/nltk/gameofthrones/A Storm of Swords - Book 3 - Book 3.txt"))
    with open(os.path.expanduser(mypath), 'rU') as f:
    	raw = f.read()
    return raw

def make_tokens(rawdata):
    tokens = nltk.word_tokenize(rawdata)
    mytext = nltk.Text(tokens)
    return mytext

def graph_dispersion(mytext, *args):
    mylist=[]
    for index, items in enumerate(args):
        mylist.append(items)
    mytext.dispersion_plot(mylist)

def lexical_diversity(mytext):
    return len(mytext) / len(set(mytext))

if __name__ == "__main__":
    book1 = load_file('~/GitHub/Python/nltk/gameofthrones/A Game of Thrones - Book 1 - Book 1.txt')
    book2 = load_file('~/GitHub/Python/nltk/gameofthrones/A Clash of Kings - Book 2 - Book 2.txt')
    book3 = load_file('~/GitHub/Python/nltk/gameofthrones/A Storm of Swords - Book 3 - Book 3.txt')
    book4 = load_file('~/GitHub/Python/nltk/gameofthrones/A Feast for Crows - Book 4 - Book 4.txt')
    book5 = load_file('~/GitHub/Python/nltk/gameofthrones/A Dance With Dragons - Book 5 - Book 5.txt')

    book1text = make_tokens(book1)
    book2text = make_tokens(book2)
    book3text = make_tokens(book3)
    book4text = make_tokens(book4)
    book5text = make_tokens(book5)

    # How many words are in each book?
    #print len(book1text) #334146
    #print len(book2text) #363393
    #print len(book3text) #484521
    #print len(book4text) #354309
    #print len(book5text) #468984

    # What's the diversity of word use for each book?
    #print lexical_diversity(book1text)
    #print lexical_diversity(book2text)
    #print lexical_diversity(book3text)
    #print lexical_diversity(book4text)
    #print lexical_diversity(book5text)

    graph_dispersion(book1text, "Stark", "Lannister", "Greyjoy", "Baratheon", "Targaryen")

    #book1text.concordance("Jon") # shows the word in context, e.g. Robb and Jon sat tall and still on their horses, Bran's bastard brother Jon
    
    #book1text.similar("Lannister") # book1 returns "the he and her his said you man them a him in it king mountain stark had horse night not"

    #book1text.common_contexts("north", "cold")

    #book1text.generate() # Generate some random text

    #myfreqdist = nltk.FreqDist(book1text)
    #myvocab = myfreqdist.keys()
    #print myvocab[:50] # Top 50 words
    #print myfreqdist['Stark'] # how many times does this word occur
    #myfreqdist.plot(50, cumulative=True) # Plots the frequency dist of first 50 words, Note: must be words

    #myfreqdist = [w for w in set(book1text) if len(w)>5]
    #print sorted(myfreqdist)
