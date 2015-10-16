from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Video(models.Model):
    video_id = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name


class Object(models.Model):
    object_id = models.IntegerField(default=0)
    object_name = models.CharField(max_length=200)
    video = models.ForeignKey(Video)
    def __unicode__(self):
        return self.object_name

class User(models.Model):
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class UserAction(models.Model):
    type = models.IntegerField(default=0)
    object = models.ForeignKey(Object)
    user = models.ForeignKey(User)
