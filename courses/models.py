from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from taggit.managers import TaggableManager

class Course(models.Model):
  # might create an index later if needed
  title = models.CharField(max_length=200)
  overview = MarkdownxField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  # might use thumbnail later
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  video_link = models.URLField(null=True, blank=True)
  owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  slug = models.SlugField(max_length=200, unique=True)
  created = models.DateTimeField(auto_now_add=True)
  tags = TaggableManager()
  
  class Meta:
    ordering = ['-created']
    
  def __str__(self):
    return self.title

class Week(models.Model):
  title = models.CharField(max_length=200)
  description = MarkdownxField()
  course = models.ForeignKey(Course, related_name='weeks', on_delete=models.CASCADE)
  # week needs to be ordered maybe javascript will do the job
  
  def __str__(self):
    return self.title

# class Review(models.Model):
#   user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#   course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
#   # add validation if needed later
#   rating = models.DecimalField(max_digits=3, decimal_places=2)
#   comment = MarkdownxField()
#   course = models.ForeignKey(Course, on_delete=models.CASCADE)
#   created_at = models.DateTimeField(auto_now_add=True)
  
#   def __str__(self):
#     return f'{self.course.title} - {self.rating}'


