from django.db import models
from django.contrib.auth.models import User
from dealerapp.models import property
# Create your models here.
class bookingrequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prop = models.ForeignKey(property, on_delete=models.CASCADE)

class feedback(models.Model):
   name = models.CharField(max_length=20)
   email = models.CharField(max_length=30)
   subject = models.CharField(max_length=50)
   message = models.TextField(max_length=50)