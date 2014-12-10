import mechanize
import cookielib

# Mechanize Cheat Sheet: https://views.scraperwiki.com/run/python_mechanize_cheat_sheet/

# Login Info
USERNAME = ''
PASSWORD = ''

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()

def initialize_browser():
    br.set_cookiejar(cj) # Set cookie car

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # Want debugging messages?
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)

    # User-Agent - Pretend to be Chrome browser
    br.addheaders = [('User-agent', 'Chrome')]


def open_link(mylink):
    # Open up some site
    #br.open('http://google.com')
    br.open(mylink)

    # Show the source
    print br.response().read()

    # Show the HTML title
    #print br.title() # E.g: Google

    # Show the response headers
    #print br.response().info()

    # Inspect name of the form
    for myform in br.forms():
        print myform

    # Select the specific form you want
    br.select_form(nr=0) #Form is TextControl (username),

    # User credentials, select by 'input name'
    #br.form['ctl0$Content$txtUserName'] = USERNAME
    #br.form['ctl0$Content$txtPassword'] = PASSWORD

    # Login
    #br.submit()
    ## You are now logged in!

def write_data(mylocation, mylink):
    text_file = open(mylocation, "w")
    r = br.open(mylink).read()
    text_file.write(r)
    text_file.close()

if __name__ == '__main__':

    initialize_browser()
    open_link('https://www.google.com/finance/historical?cid=22144&startdate=Jan+1%2C+2013&enddate=Jan+16%2C+2014&num=30&ei=TGLYUtjxFqGK6gHj5QE')

    write_data("stock.csv", "https://www.google.com/finance/historical?cid=22144&startdate=Jan+1%2C+2013&enddate=Jan+16%2C+2014&num=30&ei=TGLYUtjxFqGK6gHj5QE")

    print "Writing apple stock page"
