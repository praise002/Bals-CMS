from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
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

class Content(models.Model):
  week = models.ForeignKey(Week, related_name='contents',on_delete=models.CASCADE)
  content_type = models.ForeignKey(ContentType, 
                                  on_delete=models.CASCADE,
                                  limit_choices_to={'model__in':(
                                                    'text',
                                                    'video',
                                                    'image',
                                                    'file')})
  object_id = models.PositiveIntegerField()
  item = GenericForeignKey('content_type', 'object_id')
  
class ItemBase(models.Model):
  owner = models.ForeignKey('auth.User', related_name='%(class)s_related', on_delete=models.CASCADE)
  # might need to remove title later
  title = models.CharField(max_length=250)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  class Meta:
    abstract = True
    
  def __str__(self):
    return self.title

class Text(ItemBase):
  content = models.TextField()
  
class File(ItemBase):
  file = models.FileField(upload_to='files')
  
class Image(ItemBase):
  file = models.FileField(upload_to='images')
  
class Video(ItemBase):
  url = models.URLField()



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