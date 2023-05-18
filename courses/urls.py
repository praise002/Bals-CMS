from django.urls import path
from . views import CourseListAPIView, CourseDetailAPIView, WeekListAPIView

app_name = 'courses'

urlpatterns = [
  path('', CourseListAPIView.as_view(), name='course_list'),
  path('<slug:slug>/', CourseDetailAPIView.as_view(), name='course_detail'),
]