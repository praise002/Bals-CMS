from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Course, Week, Content, Text, File, Image, Video


class WeekInline(admin.StackedInline):
  model = Week

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ['title', 'created']
  list_filter = ['created']
  search_fields = ['title', 'overview']
  prepopulated_fields = {'slug': ('title',)}
  inlines = [WeekInline]

class ContentInline(GenericTabularInline):
  model = Content
  
@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
  inlines = [ContentInline]

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
  inlines = [ContentInline]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
  inlines = [ContentInline]
  
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
  inlines = [ContentInline]