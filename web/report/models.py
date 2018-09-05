from django.db import models
from django.contrib.auth.models import User
from web import settings

# Create your models here.
#All models are subclass of the django.db.models.Model class
#Each class will be transformed into database tables
#fields CharField, DateTimeField, etc., are all subclasses of django.db.models.Field and they come included in the Django core – ready to be used.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)  #it will enforce the uniqueness of the field at the database level.
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics',on_delete=models.CASCADE,)
    starter = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE,)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE,)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.message

#Board.objects.get(id=1) = get for a specific id
#board = Board() = instantiate a database
#Board.objects.create(name='...', description='...') = Create and save an object in the database
#Board.objects.all() = List all objects

class Item(models.Model):
   name = models.CharField(max_length=255)
   brand = models.CharField(max_length=255)
   oldprice  = models.CharField(max_length=255)
   newprice = models.CharField(max_length=255)

   def __str__(self):
    return self.name
