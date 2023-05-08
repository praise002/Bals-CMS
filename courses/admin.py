from django.contrib import admin
from .models import Course, Week


class WeekInline(admin.StackedInline):
  model = Week

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ['title', 'created']
  list_filter = ['created']
  search_fields = ['title', 'overview']
  prepopulated_fields = {'slug': ('title',)}
  inlines = [WeekInline]


