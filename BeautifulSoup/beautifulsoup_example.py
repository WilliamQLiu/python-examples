### Beautiful Soup Example

from bs4 import BeautifulSoup # For using BeautifulSoup
from bs4 import UnicodeDammit # For using Unicode Converter 
import re # For Regular Expressions example

### HTML data that we'll parse (can be string or an actual .html file)
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and 
their names were:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

def select_data_structure(mysoup):
    ### Examples of how to navigate the HTML structure with BS
    print "Title: ", mysoup.title # <title>The Dormouse's story</title>
    print "Title Name:", mysoup.title.name # title
    print "Title Parent Name:", mysoup.title.parent.name # head
    print "Paragraph:", mysoup.p
    # <p class="title"><b>The Doormouse's story</b></p>
    print "Class of Paragraph:", mysoup.p['class'] # ['title']
    print "Links:", soup.a
    print "All Links:\n", soup.find_all('a')
    # [<a class="sister" href="http://example.com/elise" id="link1">Elise</a>
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    print "Find by ID:", soup.find(id="link3")
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


def common_tasks(mysoup):
    ### Extract all the URLs found within a page's <a> tags
    for link in soup.find_all('a'):
        print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

    ### Extract all the text from a page
    print(soup.get_text())
    # The Dormouse's story
    #
    # The Dormouse's story
    # Once upon a time there were three little sisters; and
    # their names were:
    # Elsie,
    # Lacie and
    # Tillie;
    # and they lived at the bottom of a well.
    # ...


def tag_example():
    # A BeautifulSoup object represents the document as a whole
    # Treat as a Tag, supports most of the navigating/searching the tree methods

    # A Tag object corresponds to an XML or HTML tag in the original document
    soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
    mytag = soup.b # Make tag from b tags
    print "The Tag is:", mytag # <b class="boldest">Extremely bold<b>
    print "Tag name:", mytag.name # b

    # A Tag object has many attributes, treat it like a dictionary
    print "Tag Attributes:", mytag.attrs # {'class': ['boldest']}
    print "Tag's class:", mytag['class'] #['boldest']

    # You can add, remove, and modify a tag's attributes
    mytag['class'] = 'verybold' # modify a tag
    mytag['id'] = 1 # add an attribute
    print "Added and modified attribute on Tag:", mytag
    del mytag['class']
    print "Deleted attribute on Tag:", mytag

    # Some HTML attributes can have multiple values (e.g. class)
    # Attribute 'class' can have more than one CSS class, in BS shows as a list
    css_soup = BeautifulSoup('<p class="body"></p>') # Single class
    print "Soup with single class:", css_soup.p['class'] # ['body']
    css_soup = BeautifulSoup('<p class="body strikeout"></p>') # Two classes
    print "Soup with two classes:", css_soup.p['class'] # ["body", "strikeout"]
 
    # If a tag attribute looks like multi-valued attributes, but its defined by
    # HTML standards as a single value, the attribute remains a single value
    id_soup = BeautifulSoup('<p id="my id"></p>')
    # ID is single attribute, but given as a multi-value
    print "Unknown Attribute Example:", id_soup.p['id'] #Keeps as single value

    # If parsing a document as XML, there are no multi-valued attributes
    xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
    print "Parsing XML always returns single value:", xml_soup.p['class']
    # [body strikeout] # See how it returns as one large string instead of list


def navigablestring_example(mysoup):
    # NavigableString class adds navigation to a String (allows up, down, etc.)

    soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
    mytag = soup.b # Make tag from b tags

    ### Strings correspond to text within a tag using NavigableString class
    # If only one string, then use .string; if two+ strings, use .strings

    # Example - Only one string in Tag, use .string
    print "\nString of Tag:", mytag.string # Extremely bold
    print "Type of tag.string:", type(mytag.string)
    # <class 'bs4.element.NavigableString'
    print "Converting tag.string element back to Unicode string:", \
        unicode(mytag.string)
    print "Type of tag.string:", type(unicode(mytag.string)) # <type 'unicode'>

    # Example - 2+ strings in Tag, can iterate through using .strings
    print "Iterating through all strings using .strings"
    for string in mysoup.strings:
        print (repr(string))
    #\n
    #The Dormouse's story
    # ...

    # Example - 2+ strings in Tag, can iterate through using .stripped_strings
    # with the added benefit of ignore all whitespace
    print "Iterating through all strings using .stripped_strings"
    for string in mysoup.stripped_strings:
        print (repr(string))
    #The Dormouse's story
    #The Dormouse's story
    #Once upon a time there were three little sisters...

    ### Comment object is a subclass of the NavigableString class
    markup = "<b><!--Hey, buddy.  Want to buy a used parser?--></b>"
    soup = BeautifulSoup(markup)
    comment = soup.b.string
    print "Comment Type:", type(comment) # <class 'bs4.element.Comment'>
    print "Comment:", comment # Hey, buddy. Want to buy a used parser?


def navigate_data_structure_as_tree(mysoup):
    # How to navigate the parse tree of a Soup
    
    print "Select HTML tags (head):", mysoup.head
    # <head><title>The Dormouse's story</title></head>
    print "Zoom in on HTML tags (body.b):", mysoup.body.b 
    # <b>The Dormouse's story</b>
    print "Get all tags:", mysoup.find_all('a'), "\n" # Get all links

    # Get tag's children available through .contents and returns a list
    head_tag = mysoup.head
    print "\nTag's children (head):", head_tag.contents
    # [<title>The Dormouse's story</title>]
    title_tag = head_tag.contents[0] #Contents are available as a list
    print "Tag's children (title)", title_tag.contents
    # [u"The Dormouse's story"]

    for child in head_tag.children:
        print(child)
    #<title>The Dormouse's story</title>

    ### Can navigate down (.contents, .children, .descendants), 
    ### up (.parent, .parents) and sideways (.next_sibling, .previous_sibling)

    ### Can also navigate by CSS class
    # Can also use CSS selectors by passing in string to the .select() method
    mysoup.select("title")


def find_all_example(mysoup):
    # Find tags by filtering on a string, regular expression, list, or function
    
    ### Find with just a string
    print "Finding tags by string, using tag 'b':", mysoup.find_all('b')
    # [<b>The Dormouse's story</b>]
    print "Finding tags by string, using id:", mysoup.find_all(id='link2')
    # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

    ### Find with a regular expression (acts like a match() method)
    print "Finding tags by regex for tags starting with 'b':"
    for mytag in soup.find_all(re.compile("^b")):
        print(mytag.name) # Finds names that start with 'b'
    # body
    # b

    ### Find using a list, matches against any item in that list
    print "Finding with a list", soup.find_all(["a", "b"])
    # <b>The Dormouse's story</b>,
    # <a class="sister" href="http://example.com/elsie", id="link1">Elsie</a>

    ### Function (if the above methods don't work), element as the only
    # argument and should return True (if matches) or False (if no match)
    # See Documentation


def unicode_dammit_example():
    # Install the 'chardet' or 'cchardet' Python libraries for better guesses

    ### Take a string with unknown encoding and make the string Unicode
    weirdass_string = "Sacr\xc3\xa9 bleu!"
    dammit = UnicodeDammit(weirdass_string)
    print "Original Word with weird encoding:", weirdass_string
    print "Dammit Print:", (dammit.unicode_markup)
    print "Dammit Type:", (dammit.original_encoding)

    ### Take a doc with mostly UTF-8 encoding (and misc encodings due to mult
    # data sources) and convert to UTF-8 Unicode with .Dammit.detwingle()
    snowmen = (u"\N{SNOWMAN}" * 3)
    quote = (u"\N{LEFT DOUBLE QUOTATION MARK}I like snowmen!\N{RIGHT DOUBLE QUOTATION MARK}")
    doc = snowmen.encode("utf8") + quote.encode("windows-1252")
    # So now we have one doc with two encodings in it, printing is a mess
    #print "Weird Decoding doc with utf8:", doc # messed up, won't print
    #print (doc.decode("windows-1252")) # So messed up it doesn't even print

    # Decode using UnicodeDammit.detwingle() converts the string to pure UTF-8
    new_doc = UnicodeDammit.detwingle(doc)
    print new_doc.decode("utf8")

if __name__ == '__main__':
    
    ### Setup soup with string of HTML structure and defining a parser
    soup = BeautifulSoup(html_doc, "html.parser")
    # Multiple parsers including:
    #   "html.parser" is Python's HTML Parser
    #   'lxml' and 'xml' is library lxml's HTML and XML Parser
    #   'html5lib' is same parsing as a web browser, creates valid HTML5

    ### Print the contents of the soup (HTML) 
    print(soup.prettify() + "\n") # Print out the soup in pretty print

    ### Beautiful Soup transforms HTML doc into 4 kinds of objects:
    ### 1.) BeautifulSoup, 2.) Tag, 3.) NavigableString, 4.) Comment
    
    ### 1.) BeautifulSoup and 2.) Tag Example
    #tag_example()

    ### 3.) Navigable String and 4.) Comment Example
    #navigablestring_example(soup)

    ### How to select HTML tags
    #select_data_structure(soup) # Examples of how to select HTML structure
    
    ### Navigate the data structure as a tree (go up, down, sideways)
    #navigate_data_structure_as_tree(soup)

    ### Find all and filter by a string, a regular expression, list or function
    #find_all_example(soup)

    ### Commonly used tasks (for extracting data)
    #common_tasks(soup) # Commons tasks like extracting all URLS and text

    ### Unicode, Dammit is used whenever you want to convert unknown encoding
    # to straight Unicode
    unicode_dammit_example()