"""
    Download data about asteroids from asterank API
    We are mainly interested in diameter, profit, last_obs, closeness, name,
    clas
"""


import json
import requests
import pandas as pd


JSON_FILE = 'asteroid_list.json'


def request_from_api(url):
    """ Download data about asteroids from asterank API """
    read_timeout = 1.0
    try:
        r = requests.get(url, timeout=(20.0, read_timeout),
                         allow_redirects=True)
    except requests.exceptions.ReadTimeout as e:
        print "Waited too long between bytes", e
    print "Response Code is: ", r.status_code
    print "Headers are: ", r.headers
    print "JSON response is: ", r.json
    print "Text is: ", r.text

    obj = open(JSON_FILE, 'wb')  # Write to file
    obj.write(r.text)
    obj.close


def convert_json_csv(location):
    """ Convert file from JSON to csv """
    json_data = open(location)
    loaded_data = json.load(json_data)
    df = pd.io.json.json_normalize(loaded_data)

    #print df
    df.to_csv('asteroid_list.csv')


if __name__ == '__main__':

    #url = 'http://www.asterank.com/api/asterank?query={"e":{"$lt":0.1},"i":{"$lt":4},"a":{"$lt":1.5}}&limit=1'
    #url = 'http://www.asterank.com/api/asterank?query={}&limit=5'
    #request_from_api(url)
    convert_json_csv('asteroid_list_all.json')
