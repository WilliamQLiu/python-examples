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


# A simple serializer
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


# Serializer that returns complete object instances with .create() and update()
class InstanceCommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()  # if 'Comment' was a Django Model, need to save obj
        return instance


if __name__ == '__main__':

    # Create a simple object
    comment = Comment(email='wliu@test.com', content='foo bar')

    # Create a serializer to serialize and deserialize data corresponding
    # to the Comment objects

    ### SERIALIZE
    serializer = CommentSerializer(comment)  # Serialize a comment
    print serializer.data  # Take model, translate into Python native datatypes
    # {'email': u'wliu@test.com', 'content': u'foo bar',
    # 'created': datetime.datetime(2014, 10, 9, 16, 20, 9, 822774)}

    # Finalize the serialization process by rendering the data into JSON
    json = JSONRenderer().render(serializer.data)
    print "JSON is " + json
    # # '{"email": "wliu@test.com", "content": "foo bar",
    #"created": "2014-10-9T16:20:09.822"}'

    ### DESERIALIZE
    stream = StringIO(json)
    data = JSONParser().parse(stream)  # Parse stream to Python native datatype

    serializer = CommentSerializer(data=data)  # Restore native datatypes into a dic of validated data
    serializer.is_valid()  # True  # Call is_valid() before accessing data
    serializer.validated_data
    # # {'content': 'foo bar', 'email': 'wliu@test.com',
    #'created': datetime.datetime(2014, 10, 9, 16, 20, 09, 822243)}


    ### INSTANCES
    # If we want to return complete object instances based on validated data
    # we need to implement .create() and update() methods


