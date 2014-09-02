""" JSON (Javascript Object Notation) is a lightweight data-interchange format
    JSON is built on two structures:
      * A collection of name/value pairs (e.g. an object, record, dic, table, etc)
      * An ordered list of values (e.g. an array, vector, list, or sequence)

      An object is an unordered set of name/value pairs.  An object begins with
      { left brace and ends with right brace }.  Each name is followed by : (color)
      and the name/value pairs are separated by , (comma)
"""

import json


def encoding_basic_python_object():
    print "Example 1:"
    a = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    print type(a)  #<type 'str'>
    print a  # ["foo", {"bar": ["baz", null, 1.0, 2]}]

    print "Example 2:"
    b = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
    print type(b)  #<type 'str'>
    print b  # {"a": 0, "b": 0, "c": 0}


def compact_encoding():
    print "Example 1:"
    c = json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',', ':'))
    print type(c)  #<type 'str'>
    print c  # [1,2,3,{"4":5,"6":7}]


def pretty_print():
    print "Example 1:"
    d = json.dumps({'4': 5, '6': 7}, sort_keys=True,
                   indent=2, separators=(',', ':'))
    print type(d)  #<type 'str'>
    print d
    #{
    #  "4":5,
    #  "6":7,
    #}


def decoding_JSON():
    print "Example 1:"
    e = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
    print type(e)  #<type 'list'>
    print e  #[u'foo', {u'bar': u['baz', None, 1.0, 2]}]


#For specializing_JSON_object_decoding() example
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


def specializing_JSON_object_decoding():
    print "Example 1:"
    print json.loads('{"__complex__": true, "real": 1, "imag": 2}',
                 object_hook=as_complex)  #(1+2j)


if __name__ == '__main__':
    encoding_basic_python_object()
    compact_encoding()
    pretty_print()
    decoding_JSON()
    specializing_JSON_object_decoding()
