"""
    For Django-Rest-Framework Serialization
    http://www.django-rest-framework.org/api-guide/serializers/

    SERIALIZATION
    Serializers allow you to convert complex data (e.g. querysets and model
    instances) into native Python datatypes that can then be easily rendered
    into JSON, XML or other types.

    DESERIALIZATION
    Serializers also provide deserialization, allowing parsed data to be
    converted back into complex types, after first validating the incoming data

    TYPES OF SERIALIZERS
    DRF's main types of Serializers are:
        serializers.Serializer -
        serializers.ModelSerializer - maps to Django model definitions
            * is the same as Serializer class above
            * automatically generates set of fields based on the model
            * automatically generates validators for serializer
            * includes simple implementations of .create() and .update()
            * By default, uses primary key (PrimaryKeyRelatedField) to represent relationships
        serializers.HyperlinkedModelSerializer
            * Similar to ModelSerializer class except it uses hyperlinks to represent relationships
            * Hyperlinks are serializers.HyperlinkedRelatedField
        serializers.ListSerializer
            * Provides behavior for serializing and validating multiple objects at once
            * Usually you don't need this, can just pass 'many=True' when instantiating a serializer
            *  ListSerializer does not support multiple updates (needs to be done explicitly)
        serializers.BaseSerializer
            * Allows support alternative serialization and deserialization styles
            * BaseSerializer provides the same interface as the Serializer class
            * Can use with existing generic class based views (like with Serializer class)
            * Main difference is that BaseSerializer won't generate HTML forms in the browsable API
            * Basic API like the Serializer class, with:
                .data - returns the outgoing primitive representation
                .is_valid() - deserializes and validates incoming data
                .validated_data - returns the validated incoming data
                .errors - returns an error during validation
                .save() - persists the validated data into an object instance
            * These four methods can be overriden:
                .to_representation() - override this to support serialization, for read operations
                .to_internal_value() - override this to support deserialization, for write operations
                .create() - override to support saving instances
                .update() - override to support saving instances

    DRF's third party types of Serializers:
        MongoEngineModelSerializer # django-rest-framework-mongoengine
        GeoGeatureModelSerializer  # django-rest-framework-gis for GeoJSON
        HStoreSerializer # django-rest-framework-hstore

"""


from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
