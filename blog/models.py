from django.db import models
from tinymce.models import HTMLField
from crum import get_current_user

class Tag(models.Model):
	name = models.CharField(max_length=15)
	slug = models.SlugField(unique=True)
    
	def __str__(self):
		return self.name

class Article(models.Model):
  author = models.ForeignKey(
    'auth.User', 
    default=get_current_user, 
    on_delete=models.CASCADE)
  date_published = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200, unique=True)
  image = models.ImageField(upload_to='images/')
  content = HTMLField()
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.title