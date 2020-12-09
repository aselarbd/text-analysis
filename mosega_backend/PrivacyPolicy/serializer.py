from rest_framework import serializers

"""
Policy objects and object serializer

"""


class PolicySerializer(serializers.Serializer):
    id = serializers.SerializerMethodField('getIDField')
    data = serializers.ListField()
    url = serializers.CharField(max_length=1000)
    title = serializers.CharField(max_length=1000)

    def getIDField(self, obj):
        if not obj.id == None:
            return obj.id
        return None


class Policy(object):
    def __init__(self, title, url, data):
        self.id = None
        self.title = title
        self.url = url
        self.data = data
