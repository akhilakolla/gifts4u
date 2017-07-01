from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key = True)
    fname = models.CharField(max_length = 100)
    mname = models.CharField(max_length = 50, null = True, blank = True, default = None)
    lname = models.CharField(max_length = 50, null = True, blank = True, default = None)
    is_registered = models.BooleanField(default = False)
@receiver(post_save, sender= User)
def create_user_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()     
class Gifts(models.Model):
   #gid = models.CharField(max_length = 50)
    qty = models.CharField(max_length = 100)
    color = models.CharField(max_length = 20)
    reviews = models.CharField(max_length = 100)
    imgname = models.CharField(max_length = 100)
    imgpath = models.CharField(max_length = 100)
    cost = models.CharField(max_length = 10)
    def __str__(self):
        return self.imgpath
class Gender(models.Model):
    #gender_id = models.CharField(max_length = 100)
    gender_type = models.CharField(max_length = 6)
    def __str__(self):
        return self.gender_type
class Occasion(models.Model):
   # occasion_id = models.CharField(max_length = 50)
    occasion_type = models.CharField(max_length = 40)
    def __str__(self):
        return self.occasion_type
class Category(models.Model):
    # category_id = models.CharField(max_length = 50)
     category_type = models.CharField(max_length = 40)
     def __str__(self):
         return self.category_type
class Relationship(models.Model):
    # relation_id = models.CharField(max_length = 50)
     relation_type = models.CharField(max_length = 40)
     def __str__(self):
         return self.relation_type
 
