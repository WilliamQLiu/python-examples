"""
    Elasticsearch is a full text search engine that is distributed (
    organizes information into clusters of nodes so it can run on multiple
    servers) and is real-time (data is indexed, get responses to queries
    really fast).  The main problems ES solves are exploring data (e.g. avgs)
    and solving searches.  ES is built off of Lucene.

    Concept behind ES:
    1.) Create an ES index
    2.) Feed the index with data
    3.) Retrieve search results

    http://blog.tryolabs.com/2015/02/17/python-elasticsearch-first-steps/

    Running ES
    1.) Make sure Elasticsearch is installed, then start ES:
        Unix: $bin/elasticsearch
        Windows: $bin/elasticsearch.bat  (Note: may have to set JAVA_HOME var)
        Mac: $elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml
    2.) Verify ES is working with $curl -X GET http://localhost:9200
          Can also verify by visitin page on: http://localhost:9200/
        Should get back the following message:
        {
            status: 200,
            name: "Antiphon the Overseer",
            cluster_name: "elasticsearch",
            version: {
            number: "1.4.4",
            build_hash: "c88f77ffc81301dfa9dfd81ca2232f09588bd512",
            build_timestamp: "2015-02-19T13:05:36Z",
            build_snapshot: false,
            lucene_version: "4.10.3"
            },
            tagline: "You Know, for Search"
        }
    3.) Can add additional nodes: $bin/elasticsearch -Des.node.name=Node-2
        This automatically detects old node as its master then joins cluster
        New node is available at next port (e.g. 9201): http://localhost:9201

    Full range of queries here:
    http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl-queries.html

"""

from datetime import datetime
from elasticsearch import Elasticsearch
import requests  # to check ES is up and running
import json  # to get json responses from API
import time  # for sleep so we don't slam some person's servers
#import certifi  # use certifi for CA certificates and http auth


def simplest_es_example(es):
    """ Simplest ES example """

    # datetimes will be serialized
    es.index(index='my-index', doc_type='test-type', id=42,
             body={"any": "data", "timestamp": datetime.now()})
    # datetimes will not be deserialized
    print es.get(index='my-index', doc_type='test-type', id=42)['_source']
    # {u'timestamp': u'2015-02-20T11:26:49.484000', u'any': u'data'}


def tutorial_elasticsearchpy(es):
    """
        http://elasticsearch-py.readthedocs.org/en/master/
    """

    # Make some fake data
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime(2010, 10, 10, 10, 10, 10)
    }

    res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
    print res['created']  # False

    res = es.get(index="test-index", doc_type="tweet", id=1)
    print res['_source']
    # {u'text': u'Elasticsearch: cool. bonsai cool.', u'author': u'kimchy', u'timestamp': u'2010-10-10T10:10:10'}

    es.indices.refresh(index="test-index")

    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print "Got %d Hits:" % res['hits']['total']  # Got 1 Hits

    for hit in res['hits']['hits']:
        print ("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
    #2010-10-10T10:10:10 kimchy: Elasticsearch: cool. bonsai cool.

def starwars_example(es, r, i):
    """
        Iterate through Star Wars API swapi.co request r and use ES to index
        starting with i
    """

    while r.status_code == 200:
        r = requests.get('http://swapi.co/api/people/'+str(i))
        es.index(index='sw', doc_type='people', id=i,
                 body=json.loads(r.content))
        i = i + 1
    print("Total items:", i)  # displays number of items in index (e.g. 18)

    return es


if __name__ == '__main__':

    r = requests.get('http://localhost:9200')  # Verify ES is running
    #print(r.content)  # Should return the verification msg in step 2

    # Connect to ES; default connection is: localhost:9200
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    # Can also connect using SSL for secure connections
    """
    es = Elasticsearch(
        ['localhost', 'otherhost'],
        http_auth=('user', 'secret'),
        port=443,
        use_ssl=True,
        verify_certs=True,
        ca_certs=certifi.where(),)
    """

    #simplest_es_example(es)

    tutorial_elasticsearchpy(es)

    """

    # Star Wars Example

    # Run ES with first node, get first few indexes
    r = requests.get('http://localhost:9200')  # use node one
    node1 = starwars_example(es, r, 1)
    print node1.get(index='sw', doc_type='people', id=5)

    time.sleep(2)  # don't slam servers

    # Run ES with second node, get more indexes (make sure 2nd node is running)
    r = requests.get('http://localhost:9201')  # use node two, comment if none
    #r = requests.get('http://localhost:9200')
    node2 = starwars_example(es, r, 18)
    print node2.get(index='sw', doc_type='people', id=20)

    ### Doing search (match) with ES
    # Search to return back 'Darth Vader' and 'Darth Maul' (if 2nd node running)
    print node2.search(index='sw', body={'query': {'match': {'name': 'Darth Vader'}}})
    # Shows '_score' of 3.0426335 match for 'Darth Vader' on single node

    ### Doing search (prefix) with ES
    print node2.search(index='sw', body={'query': {'prefix': {'name': 'lu' }}})
    # Returns 'Luke Skywalker' and 'Luminara Unduli' with same score 1.0

    ### Doing search (fuzzy) with ES
    print node2.search(index='sw', body={'query': {'fuzzy_like_this_field': {'name': {'like_text': 'jaba', 'max_query_terms': 5}}}})
    # Jabba appears even though we spelled it incorrectly

    """