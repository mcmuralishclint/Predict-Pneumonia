from django.db import models
from django.contrib.auth.models import User

class UploadImage(models.Model):
    #user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='documents/%Y/%m/%d')