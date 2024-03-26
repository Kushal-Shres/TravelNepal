import image as image
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

from travelnepal import settings

GENDER_CHOICES = (
            ('Male','Male'),
            ('Female','Female'),
            ('Other','Other')
        )


class Tourist(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = MultiSelectField(choices=GENDER_CHOICES,max_choices=1,default='Male')
    email = models.CharField(max_length=50)
    country = CountryField()

    # @receiver(post_save, sender=User)
    # def update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Tourist.objects.create(user=instance)
    #     instance.travel.save()




Category = (
    ('Wilderness','Wilderness'),
    ('Religious','Religious'),
    ('Mountain','Mountain'),
    ('Trekking','Trekking'),
    ('Adventure','Adventure'),
)


class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    itinerary = models.TextField(max_length=1000)
    category = MultiSelectField(choices= Category)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0,max_length=5)
    description = models.TextField(max_length='1000')
    image = models.ImageField(upload_to='photo', blank=True, verbose_name='Place image')


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name




class Pivot(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    tourist = models.ForeignKey(Tourist,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)


class Hotel(models.Model):
    Hotel_name = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Contact = models.IntegerField(default=0)
    website = models.CharField(max_length=20)
    rating = models.FloatField(default=0.0)







