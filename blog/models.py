from django.db import models

# Create your models here.
class Post(models.Model):

  STATUS = (
    (0, "draft") ,
    (1, "published") ,
  )
  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)

  def __str__(self):
    return f"{self.title} created at {self.created_on} and updated {self.updated_on}"
