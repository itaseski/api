from importlib.metadata import requires
from urllib import response
from movies.models import WatchList, StreamPlatform
from movies.api.serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


class StreamPlatformAV(APIView):

    def get(self, request):
        """
        Return a list of all Stream Platforms.
        """
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        """
        Post a Stream Platform in a Stream Platform list.
        """
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetail(APIView):
    """
    Return a Stream Platform detailes.
    """
    def get(self, request, pk):
        """
        Return a Stream Platform.
        """
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error' : 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(stream_platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Edit a movie.
        """
        stream_platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Deleta a movie.
        """
        stream_platform = StreamPlatform.objects.get(pk=pk)
        stream_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        """
        Return a list of all movies.
        """
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        """
        Post a movie in a movies list.
        """
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetail(APIView):
    """
    Return a movie detailes.
    """
    def get(self, request, pk):
        """
        Return a  movie.
        """
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error' : 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Edit a movie.
        """
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Deleta a movie.
        """
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


