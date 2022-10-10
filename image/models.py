import django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(null=True, blank=True)
    mobile_no = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return(self.username)


class Images(models.Model):
    upload = models.ImageField(upload_to ='uploads/')
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=None,**kwargs):
    if created:
        Token.objects.create(user =instance)