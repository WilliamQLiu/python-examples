### Beautiful Soup Example

from bs4 import BeautifulSoup

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

def navigate_data_structure(mysoup):
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
    # A Tag object corresponds to an XML or HTML tag in the original document
    soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
    mytag = soup.b
    print "Tag name:", mytag.name # b

    # A Tag object has many attributes
    print "Tag Attributes:", mytag.attrs
    print "Tag's class:", mytag['class']


if __name__ == '__main__':
    
    # Setup soup with string of HTML structure and defining a parser
    soup = BeautifulSoup(html_doc, "html.parser")
    # Multiple parsers including:
    #   "html.parser" is Python's HTML Parser
    #   'lxml' and 'xml' is library lxml's HTML and XML Parser
    #   'html5lib' is same parsing as a web browser, creates valid HTML5

    print(soup.prettify() + "\n") # Print out the soup in pretty print
    
    #navigate_data_structure(soup) # Examples of how to navigate HTML structure
    #common_tasks(soup) # Commons tasks like extracting all URLS and text

    # Beautiful Soup transforms HTML doc into 4 kinds of objects:
    # Tag, NavigableString, BeautifulSoup, Comment
    tag_example()