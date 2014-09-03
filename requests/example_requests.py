""" Using Python's requests library """

import json
import requests


def get_webpage_details(site):
    """ GET details of a request """
    r = requests.get(site)
    print "Status Code: ", r.status_code
    #print r.headers  # Gets all headers as a dict
    print "Get specific field (e.g. 'content-type'):", r.headers['content-type']  # Get specific field
    print "Get encoding: ", r.encoding
    #print "Get Text: ", r.text  # Get all text of page
    print "Get JSON: ", r.json()  #
    print "GET Response Code: ", r.status_code


def request_API_calls():
    """ Using all HTTP request types (POST, PUT, DELETE, HEAD, OPTIONS) """
    r = requests.post('http://httpbin.org/post')  # Example of POST
    print "POST: ", r
    r = requests.put('http://httpbin.org/put')  # Example of PUT
    print "PUT: ", r
    r = requests.delete('http://httpbin.org/delete')  # Example of DELETE
    print "DELETE: ", r
    r = requests.head('http://httpbin.org/get')  # Example of HEAD
    print "HEAD: ", r
    r = requests.options('http://httpbin.org/get')  # Example of OPTIONS
    print "OPTIONS: ", r


def pass_params_in_urls():
    """ How to pass data in the URL's query string
        By hand, getting URL would be given as key/value pairs in the URL
        after the question mark (e.g. httpbin.org/get?key=val)
    """

    # If you want to pass 'key1=value1' and 'key2=value2' to 'httpbin.org/get'
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params=payload)

    # Verify that URL has been encoded correctly by printing out URL
    print "URL is: ", r.url  # http://httpbin.org/get?key2=value2&key1=value1


def pass_headers_in_request():
    """ Add HTTP headers to a request by adding a dict to the 'headers' param """
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


if __name__ == '__main__':
    #get_webpage_details('https://api.github.com/events')
    #request_API_calls()
    #pass_params_in_urls()
    pass_headers_in_request()
    #response_content()
    #json_response_content()


