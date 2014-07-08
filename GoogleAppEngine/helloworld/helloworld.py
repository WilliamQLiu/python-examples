from google.appengine.api import users

import webapp2

#form="""
#<form action="/testform">
#    <input name="q">
#    <input type="submit">
#</form>
#"""

form="""
<form method="post" action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)
        #user = users.get_current_user() # If User is already signed in, gets the current user's name
        #if user:
        #    self.response.headers['Content-Type'] = 'text/plain'
        #    self.response.write('Hello, ' + user.nickname())
        #else: # If User is unknown, redirect to Google Account sign-in        
        #    self.redirect(users.create_login_url(self.request.uri))

class TestHandler(webapp2.RequestHandler):
    def post(self):
        q = self.request.get("q")
        self.response.out.write(q)
        
    def get(self):
        q = self.request.get("q") # Get the parameter q
        self.response.out.write(q)
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(self.request)

application = webapp2.WSGIApplication([('/', MainPage),
('/testform', TestHandler)], debug=True)