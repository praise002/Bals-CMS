from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from . serializers import (CourseSerializer, 
                          WeekSerializer, ContentSerializer)
from . models import Course, Week

class CourseListAPIView(ListAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  
class CourseDetailAPIView(RetrieveAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  lookup_field = 'slug'
  lookup_url_kwarg = 'slug'
  
class WeekListAPIView(ListAPIView):
  queryset = Week.objects.all()
  serializer_class = WeekSerializer
  