from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, created, **kwargs):
#     instance.profile.save()