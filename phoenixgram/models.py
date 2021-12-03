from django.db import models

# Create your models here.
class Profile(models.Model):
  profile_photo = models.ImageField(upload_to='static/images/')
  bio = models.TextField()

class Image(models.Model):
  image = models.ImageField(upload_to='static/images/')
  image_name = models.CharField(max_length=30)
  image_caption = models.TextField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  like = models.IntegerField()
  comment = models.TextField()
  