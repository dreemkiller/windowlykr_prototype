from django.db import models


#change Lyker to Lykr.

#find place to deploy it

#API it


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

# change to VideoObject
class Object(models.Model):
    object_id = models.IntegerField(default=0)
    object_name = models.CharField(max_length=200)
    video = models.ForeignKey(Video)
    def __unicode__(self):
        return self.object_name

#class MarketingObject
#keyword/hashtag for Marketing object searchable string field
# URL field for what to do
# field for path to image file (thumbnail, gif, whatever)


#change User to Viewer
#remove "type" field
#add differ
class User(models.Model):
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

# remove image_filename
#add a field for "timestamp", x,y coordinate, video
#add keyword/hashtag field
class UserAction(models.Model):
    type = models.IntegerField(default=0)
    object = models.ForeignKey(Object)
    user = models.ForeignKey(User)
    image_filename = models.CharField(max_length=200, default = "/userdata/no_user/blank.png");
    def __unicode__(self):
        return self.user.name + " " + str(self.type) + " \'" + self.object.object_name + "\' " + self.image_filename
