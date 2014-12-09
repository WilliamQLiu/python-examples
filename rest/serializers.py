""" http://www.django-rest-framework.org/api-guide/serializers/#serializers
    Serializers allow complex data (e.g. querysets and model instances)
    to be converted to native Python datatypes that can be easily rendered
    into JSON, XML, or other types.  Serializers also provide deserialization,
    allowing parsed data to be converted back into complex types, after first
    validating the incoming data.
"""

from datetime import datetime

from rest_framework import serializers  # For serialization
from rest_framework.renderers import JSONRenderer  # For serialization
from StringIO import StringIO  # for deserilization
from rest_framework.parsers import JSONParser  # For deserialization


# A simple object
class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


if __name__ == '__main__':

    # Create a simple object
    comment = Comment(email='wliu@test.com', content='foo bar')

    # Create a serializer to serialize and deserialize data corresponding
    # to the Comment objects

    ### SERIALIZE
    serializer = CommentSerializer(comment)  # Serialize a comment
    print "Serializer data " + serializer.data  # Taken model and translated into Python native datatypes
    # {'email': u'wliu@test.com', 'content': u'foo bar',
    # 'created': datetime.datetime(2014, 10, 9, 16, 20, 9, 822774)}

    # Finalize the serialization process by rendering the data into JSON
    json = JSONRenderer().render(serializer.data)
    print "JSON is " + json
    # # '{"email": "wliu@test.com", "content": "foo bar",
    #"created": "2014-10-9T16:20:09.822"}'

    ### DESERIALIZE
    stream = StringIO(json)
    data = JSONParser().parse(stream)  # Parse a stream into Python native datatypes

    serializer = CommentSerializer(data=data)  # Restore native datatypes into a dic of validated data
    serializer.is_valid()  # True  # Need to call is_valid() before accessing data
    serializer.validated_data
    # # {'content': 'foo bar', 'email': 'wliu@test.com',
    #'created': datetime.datetime(2014, 10, 9, 16, 20, 09, 822243)}



