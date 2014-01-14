import mechanize
import cookielib

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

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

# Open up some site
#br.open('http://google.com')
br.open('http://mynetworkofcare.org/login.cfm/')

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
br.form['username'] = 'wliu'
br.form['password'] = 'putpasswordhere'

# Login
br.submit()

## You are now logged in!

#print (br.open('http://webstats.networkofcare.org:9999/report.cgi?profile=NY%20MH%20New%20York%20City').read())
text_file = open("sessions.txt", "w")
r = br.open("http://webstats.networkofcare.org:9999/report.cgi?profile=NY%20MH%20New%20York%20City&rid=1260&prefs=(admin)&n=10&vid=1102&dtc=0&bd=20131201&ed=20131231&dt=3&spview=1&splist=|1102|&x=1").read()
text_file.write(r)
text_file.close()
print "Sessions written to text file"

text_file = open("pageviews.txt", "w")
r = br.open("http://webstats.networkofcare.org:9999/report.cgi?profile=NY%20MH%20New%20York%20City&rid=1260&prefs=(admin)&n=10&vid=1103&dtc=0&bd=20131201&ed=20131231&dt=3&spview=1&splist=|1103|&x=1").read()
text_file.write(r)
text_file.close()
print "Pageviews written to text file"

"""
# The site we will navigate into, handling it's session
br.open('https://github.com/login')

# Inspect name of the form
for f in br.forms():
    print f

# Select the second (index one) form - the first form is a search query box
br.select_form(nr=1)

# User credentials
br.form['login'] = 'william.q.liu@gmail.com'
br.form['password'] = 'kulupu71'

# Login
br.submit()

print(br.open('https://github.com/settings/emails').read())
"""