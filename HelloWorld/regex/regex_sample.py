### Using Regular Expressions (regex) with Python
import re


def match_example():
    ### Determine if the RE matches at the beginning of the string
    regex = 'hello*' # the regular expression
    regex_pattern = re.compile(regex) # compile regex into a regex pattern obj
    mystring = r'the rabbit jumped the fence' # Make raw string
    
    print "Example Case 1 - No Matches"
    print "The regex is: ", regex
    print "The string we look at is : ", mystring
    print "Does pattern match string?", regex_pattern.match(mystring), "\n"
    # Output: None

    print "Example Case 2 - Matches"
    mystring = r'hellooooooo there!'
    print "The regex is: ", regex
    print "The string we look at is : ", mystring
    print "Does pattern match string?", regex_pattern.match(mystring), "\n"
    # Output: <_sre.SRE_Pattern object at 0x ...>
    return regex_pattern.match(mystring)

def search_example():
    ### Scans through string, looking for any location where RE matches
    regex = 'the' # the regular expression
    regex_pattern = re.compile(regex) # compile regex into a regex pattern obj
    mystring = r'i love me some cookies'
    
    print "Example Case 1 - No Matches"
    print "The regex is: ", regex
    print "The string we look at is : ", mystring
    print "Does pattern match string?", regex_pattern.search(mystring), "\n"
    # Output: None

    print "Example Case 2 - Matches"
    mystring = r'I think the whale farted'
    print "The regex is: ", regex
    print "The string we look at is : ", mystring
    print "Does pattern match string?", regex_pattern.search(mystring), "\n"
    # Output: <_sre.SRE_Pattern object at 0x ...>
    return regex_pattern.search(mystring)

def findall_example():
    ### Finds all substrings where the RE matches, returns as a list
    regex = 'man' # the regular expression
    regex_pattern = re.compile(regex, re.IGNORECASE) # Can pass optional params
    mystring = r'I think women are smarter than men!'
    
    print "Example Case 1 - No Matches"
    print "The regex is: ", regex
    print "The string we look at is : ", mystring
    print "Does pattern match string?", regex_pattern.findall(mystring), "\n"
    # Output: []]

    print "Example Case 2 - Matches"
    mystring = r'man, this manly mofo is named mandy (a womanly name)'
    print "The regex is: ", regex
    print "The string we look at is : ", mystring
    print "Does pattern match string?", regex_pattern.findall(mystring), "\n"
    # Output: ['man', 'man', 'man', 'man']
    return regex_pattern.findall(mystring)

def finditer_example():
    ### Finds all substrings where the RE matches, returns as an iterator
    regex = 'man' # the regular expression
    regex_pattern = re.compile(regex, re.IGNORECASE) # Can pass optional params
    mystring = r'I think women are smarter than men!'
    
    print "Example Case 1 - No Matches"
    print "The regex is: ", regex
    print "The string we look at is : ", mystring
    print "Does pattern match string?", regex_pattern.finditer(mystring), "\n"
    # Output: <callable-iterator object at 0x...>

    print "Example Case 2 - Matches"
    mystring = r'man, this manly mofo is named mandy (a womanly name)'
    print "The regex is: ", regex
    print "The string we look at is : ", mystring
    print "Does pattern match string?", regex_pattern.finditer(mystring), "\n"
    # Output: <callable-iterator object at 0x...>
    return regex_pattern.finditer(mystring)

def query_match_object(match):
    #group(), returns string matched by the RE
    print "Group (i.e. String) of matched object ", match.group()

    #start(), returns the starting position of the match
    print "Start of matched object", match.start()
    #end(), returns the ending position of the match
    print "End of matched object", match.end()

    #span() returns tuple with the (start, end) positions of the match
    print "Span (i.e. Tuple) of matched object", match.span()    

if __name__ == '__main__':

    ### 1.) Examples of Getting a match object
    m=match_example()  # Determine if RE matches at beginning of the string
    #m=search_example() # Determine if RE matches anywhere in string
    #m=findall_example() # Finds all substrings where RE matches, returns list
    #m=finditer_example() # Finds all substrings where RE matches, returns iter
    
    ### 2.) Now Query the Match Object's methods and attributes
    query_match_object(m) # Note: not all match objects can use all the methods