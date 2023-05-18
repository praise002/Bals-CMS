from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from . models import Course, Week, Text, File, Image, Video, Content

class ContentSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Content
    fields = ['order', 'item']

# text, file, image, video
class WeekSerializer(serializers.ModelSerializer):
  contents = ContentSerializer(many=True, read_only=True)
  class Meta:
    model = Week
    fields = ['order', 'title', 'description']

class CourseSerializer(serializers.ModelSerializer):
  # use_url: By setting it to True, the serializer will return the URL, allowing the client to fetch the file content separately.
  image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
  # weeks = serializers.StringRelatedField(many=True, read_only=True)
  weeks = WeekSerializer(many=True, read_only=True)
  tags = TagListSerializerField()
  
  class Meta:
    model = Course
    fields = ['id', 'title', 'overview', 'price', 'image', 'tags', 'video_link', 'owner', 'slug', 'created', 'weeks']
    read_only_fields = ['id'] 
  
