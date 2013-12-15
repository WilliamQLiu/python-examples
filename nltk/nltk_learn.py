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
    return tokens

def graph_dispersion(tokens):
    mytext = nltk.Text(tokens)
    mytext.dispersion_plot(["Stark", "Lannister", "Greyjoy", "Targaryen", "Baratheon"])

def nsyl(word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]] #return number of syllables    


if __name__ == "__main__":
    book1 = load_file('~/GitHub/Python/nltk/gameofthrones/A Game of Thrones - Book 1 - Book 1.txt')
    book2 = load_file('~/GitHub/Python/nltk/gameofthrones/A Clash of Kings - Book 2 - Book 2.txt')
    book3 = load_file('~/GitHub/Python/nltk/gameofthrones/A Storm of Swords - Book 3 - Book 3.txt')
    book4 = load_file('~/GitHub/Python/nltk/gameofthrones/A Feast for Crows - Book 4 - Book 4.txt')
    book5 = load_file('~/GitHub/Python/nltk/gameofthrones/A Dance With Dragons - Book 5 - Book 5.txt')

    book1tokens = make_tokens(book1)
    graph_dispersion(book1tokens)
    #graph_dispersion(book3)
    
