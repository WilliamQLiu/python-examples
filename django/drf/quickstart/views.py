"""
    ViewSets are classes that are basically multiple views grouped together
    with some common behavior.  We can use individual views if we want to, but
    it's not quite as concise.

    Automatic (not recommended): DRF will automatically specify a 'serializer'
    and a 'queryset' based on a 'model' attribute that you set in the ViewSet.
    This is not recommended because you want to be explicit about the API.

    Manually (recommended): You can specify the 'queryset' and the
    'serializer_class' attributes instead of a 'model' attribute.

"""


from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows users to be viewed or edited. """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows groups to be viewed or edited. """
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
