from wsgiref.validate import validator
from rest_framework import serializers
from movies.models import Movie

import re

def check_cyrillic(value):
    """
        Check if a string contains cyrillic characters
    """
    if bool(re.search('[\u0400-\u04FF]', value)):
       raise serializers.ValidationError("Name contains cyrillic character!") 


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[check_cyrillic])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new 'Movie' instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Movie' instance, given the validated data.
        """
        instance.name= validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description can't be the same!")
        return data


    def validate_name(self, value):
        """
        Check that the movie name is too short.
        """
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        return value
