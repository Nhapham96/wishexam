from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from ..login.models import *
class ListManager(models.Manager):
    def remove_item(self,postData):
        item =Mylist.objects.get(id=int(postData['item_id']))
        item.delete()
    def delete(self,postData):
        List.objects.get(id=int(postData['item_id'])).delete()
    def addding(self,postData):
        Mylist.objects.create(name=postData['item_name'],add_by=User.objects.get(id=int(postData['me'])))
    def add_validator(self,postData):
        errors = {}
        if len(postData['name']) == 0:
            errors['name'] = 'Need to have items/products to add!!'
        elif List.objects.filter(name=postData['name']).exists():
            errors['name']='This item/product already added!'
        else:
            List.objects.create(name=postData['name'],added_by=User.objects.get(id=int(postData['me'])))
            errors['success']="successfully!"
           
        return errors
class List(models.Model):
    name= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User,related_name='added') 
    objects = ListManager() 
class Mylist(models.Model):
    name= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    add_by = models.ForeignKey(User,related_name='add') 
    objects = ListManager()


