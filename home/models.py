from django.db import models
from django.contrib.auth.models import User
class UserData(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	picture = models.ImageField(upload_to = 'image_data')