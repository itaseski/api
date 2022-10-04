from rest_framework import serializers
from movies.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.HyperlinkedModelSerializer):    

    class Meta:
        model = WatchList
        fields = '__all__'



class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):

    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'




