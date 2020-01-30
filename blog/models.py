from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    profile_id = models.AutoField(primary_key=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to="blog/profile_pics")
    bio = models.CharField(max_length=150)
    address = models.CharField(max_length=100)
    bg_pic = models.ImageField(upload_to="blog/bg_pics")
    blogcount = models.IntegerField(default="0")
    fields = models.CharField(max_length=200,default="Personal Blog")

    def __str__(self):
        return self.user.username

class Pst(models.Model):
    blogger = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )
    pst_id=models.AutoField(primary_key=True)
    dop=models.DateTimeField()
    pst_text=models.CharField(max_length=150)
    likes=models.IntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)



