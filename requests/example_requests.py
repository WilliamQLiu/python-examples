"""
    The internet is basically made up of requests and responses.
    Using Python's requests library, we can look into how this works.
    http://docs.python-requests.org/en/latest/api/

    Commands
        GET
            Read an existing resource.  This is like SELECT in SQL
        HEAD
            Similar to GET except server doesn't return a message-body in
            response.  Instead, it gets the metadata of an existing resource.
        POST
            Creates a new resource.  This is like INSERT in SQL
        PUT
            Updates an existing resource.  This is like UPDATE in SQL
        PATCH
            Usually not implemented.  Updates part of an existing resource.
            This is like UPDATE in SQL
        DELETE
            Deletes an existing resource.  This is like DELETE in SQL


    Important HTTP Status Codes
        200 OK means Success
            GET - returns resource
            PUT - Provides status message or returns message
        201 Created means Success
            POST - Provides status message or returns newly created resource
        204 No Content means Success
            Completed, but nothing to return (because of no content)
        304 Unchanged means Redirect
            There's no changes since the last request (usually used to checking a field like 'Last-Modified' and 'Etag' headers, which is a mechanism for web cache validation)
        400 Bad Request means Failure
            PUT - returns error message, including form validation errors
            POST - returns error message, including form validation errors
        401 Unauthorized means Failure
            Authentication required but user did not provide credentials
        403 Forbidden means Failure
            User attempted to access restricted content
        404 Not Found means Failure
            Resource was not found
        405 Method Not Allowed means Failure
            An invalid HTTP method was attempted
        410 Gone means Failure
            A method was attempted that is no longer supported.
            E.g. mobile apps can test for this condition and if it occurs,
                 tell the user to upgrade
        500 Internal Server Error means Failure
            The server encountered an unexpected condition

    Sample API URLS
        api/v1/resume
            for GET and POST
        api/v1/resume/:slug/
            for GET, PUT, DELETE
        api/v1/job
            for GET and POST
        api/v1/job/:slug/
            for GET, PUT, DELETE
        Same goes for say api/v1/education and api/v1/experience
        slug represents a variable (e.g. the resume id)

"""

import json
import requests


def get_webpage_details(site):
    """ GET details of a request """
    r = requests.get(site)

    # Status Code
    print "GET Response Status Code: ", r.status_code  # 200

    print r.headers  # Gets all headers as a dict
    """
    {
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
    }
    """


    print "Get specific field (e.g. 'content-type'):", \
        r.headers['content-type']  # Get specific field
    # application/json; charset=utf-8

    print "Get encoding: ", r.encoding  #utf-8

    #print "Get Text: ", r.text  # Get all text of page
    #print "Get JSON: ", r.json()  # Get everything as a JSON file


def request_API_calls():
    """ Using all HTTP request types (POST, PUT, DELETE, HEAD, OPTIONS) """
    r = requests.post('http://httpbin.org/post')  # Example of POST
    print "POST: ", r  # <Response [200]>
    r = requests.put('http://httpbin.org/put')  # Example of PUT
    print "PUT: ", r  # <Response [200]>
    r = requests.delete('http://httpbin.org/delete')  # Example of DELETE
    print "DELETE: ", r  # <Response [200]>
    r = requests.head('http://httpbin.org/get')  # Example of HEAD
    print "HEAD: ", r  # <Response [200]>
    r = requests.options('http://httpbin.org/get')  # Example of OPTIONS
    print "OPTIONS: ", r  # <Response [200]>


def pass_params_in_urls():
    """
        How to pass data in the URL's query string
        By hand, getting URL would be given as key/value pairs in the URL
        after the question mark (e.g. httpbin.org/get?key=val), but instead
        we have a 'params' that we can pass a dict into
    """

    # If you want to pass 'key1=value1' and 'key2=value2' to 'httpbin.org/get'
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params=payload)

    # Again, this is the same as http://httpbin.org/get?key2=value2&key1=value1

    # Verify that URL has been encoded correctly by printing out URL
    print "URL is: ", r.url  # http://httpbin.org/get?key2=value2&key1=value1


def post_form_data_request():
    """
        If you want to send form-encoded data (like an HTML form), then
        pass a dictionary to the 'data' argument; the dict will be auto form
        encoded when the request is made
    """
    url = "http://httpbin.org/post"
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post(url, data=payload)
    print r.text  # see how data goes into 'form'

    """
    {
      "args": {},
      "data": "",
      "files": {},
      "form": {
        "key1": "value1",
        "key2": "value2"
      },
      "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "23",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.5.3 CPython/2.7.9 Darwin/14.1.0"
      },
      "json": null,
      "origin": "74.71.230.126",
      "url": "http://httpbin.org/post"
    }
    """

    # If you want to send data that is not form-encoded, pass in a string
    payload = 'This is a test'
    r = requests.post(url, data=payload)
    print r.text  # see how it goes to 'data' instead of 'form'

    """
    {
      "args": {},
      "data": "This is a test",
      "files": {},
      "form": {},
      "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "14",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.5.3 CPython/2.7.9 Darwin/14.1.0"
      },
      "json": null,
      "origin": "74.71.230.126",
      "url": "http://httpbin.org/post"
    }
    """


def pass_headers_in_request():
    """
        Add HTTP headers to a request by adding a dict to the 'headers' param
    """
    url = 'https://api.github.com/some/endpoint'
    payload = { 'some': 'data' }
    headers = { 'content-type': 'application/json' }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print r


def response_content():
    """ We can read the server's response """
    r = requests.get('https://developer.github.com/v3/activity/events/#list-public-events')
    print "Server's Response is: ", r.text

    # When you make a request, Requests makes an educated guess on encoding
    # based on the response of the HTTP headers
    print "Guessed encoding is: ", r.encoding  # utf-8
    #print "Peak at content if unsure of encoding, sometimes specified in here ", r.content


def json_response_content():
    """ There's a builtin JSON decoder for dealing with JSON data """
    r = requests.get('http://www.json-generator.com/api/json/get/bVVKnZVjpK?indent=2')
    print "Getting JSON: ", r  # Should be 200 or else if error, then 401 (Unauthorized)
    #print r.json()


def versatile_response_codes():
    """ You don't have to check for specific status codes (e.g. 200, 404) """
    url = "http://httpbin.org/post"
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print "Looks okay to me", r.status_code
    else:
        print "Doesn't look good here", r.status_code

        # We can raise an exception if there's a bad request 4XX or 5XX
        r.raise_for_status()  # Should raise http_error
        #(requests.exceptions.HTTPError:)


def accessing_cookies():
    """
        You can look at a response's cookies or send your own cookies
        to the server
    """
    # GET some cookies
    url = 'http://example.com/some/cookie/setting/url'
    r = requests.get(url)
    r.cookies['example_cookie_name']  #'example_cookie_value'

    # GET and specify your cookies
    mycookies = dict(cookies_are='working')
    r = requests.get(url, cookies=mycookies)
    r.text #'{"cookies": { "cookies_are": "working"}}'


def request_no_redirect():
    """
        By default Requests will perform redirects for all verbs except HEAD
        Use the 'history' property of the Response to track redirection
        Response.history list contains all the Response objects that
        were created (sorted oldest to most recent response)
    """

    # Redirects by default
    r = requests.get('http://github.com')  # default Requests allow redirect
    print r.url  # https://github.com/
    print r.status_code  # 200
    print r.history  #[<Response [301]>]  # Shows history of a redirect

    # Don't allow redirect
    r = requests.get('http://github.com', allow_redirects=False)
    print r.status_code  # 301
    print r.history  # []


def creating_sessions():
    """
        Session objects let you to persist certain parameters across requests.
        It also persists cookies across all requests made from the Session
        instance
    """
    s = requests.Session()

    # Sessions let cookies persist across requests
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get('http://httpbin.org/cookies')
    print r.text  # {"cookies": {"sessioncookie": 123456789}}

    # Sessions can also provide default data to the request methods
    # through providing data to the properties on a Session object
    s = requests.Session()
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})
    # both 'x-test' and 'x-test2' are sent
    s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
    print s


if __name__ == '__main__':
    #get_webpage_details('https://api.github.com/events')
    #request_API_calls()
    #pass_params_in_urls()
    #post_form_data_request()
    #pass_headers_in_request()
    #response_content()
    #json_response_content()
    #versatile_response_codes()
    #accessing_cookies()
    #request_no_redirect()
    creating_sessions()
