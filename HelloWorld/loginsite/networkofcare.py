import mechanize
import cookielib

# Login Info
USERNAME = 'wliu'
PASSWORD = 'stupid12'

# Initialize Variables

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

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Chrome')]


def open_link(mylink):
    # Open up some site
    #br.open('http://google.com')
    br.open(mylink)
    
    # Show the source
    #print br.response().read()

    # Show the HTML title
    #print br.title() # E.g: Google

    # Show the response headers
    #print br.response().info()

    # Inspect name of the form
    for myform in br.forms():
        print myform

    # Select the specific form you want
    br.select_form(nr=0) #Form is TextControl (username), 

    # User credentials
    br.form['username'] = USERNAME
    br.form['password'] = PASSWORD

    # Login
    br.submit()
    ## You are now logged in!

def write_data(mylocation, mylink):
    text_file = open(mylocation, "w")
    r = br.open(mylink).read()
    text_file.write(r)
    text_file.close()

if __name__ == '__main__':

    initialize_browser()
    open_link('http://mynetworkofcare.org/login.cfm/')
    write_data("sessions.txt", "http://webstats.networkofcare.org:9999/report.cgi?profile=NY%20MH%20New%20York%20City&rid=1260&prefs=(admin)&n=10&vid=1102&dtc=0&bd=20131201&ed=20131231&dt=3&spview=1&splist=|1102|&x=1")
    write_data("pageviews.txt", "http://webstats.networkofcare.org:9999/report.cgi?profile=NY%20MH%20New%20York%20City&rid=1260&prefs=(admin)&n=10&vid=1103&dtc=0&bd=20131201&ed=20131231&dt=3&spview=1&splist=|1103|&x=1")
