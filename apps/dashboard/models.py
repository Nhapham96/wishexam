from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from ..login.models import *
class ListManager(models.Manager):
    def remove_item(self,postData):
        me= User.objects.get(id=int(postData['user']))
        item =List.objects.get(id=int(postData['item_id']))
        me.added.remove(item)
    def delete(self,postData):
        item =List.objects.get(id=int(postData['item_id']))
        item.delete()
    def adding(self,postData):
        me = User.objects.get(id=int(postData['me']))
        item = List.objects.get(name=postData['item_name'])
        me.added.add(item)
    def add_validator(self,postData):
        errors = {}
        if len(postData['name']) == 0:
            errors['name'] = 'Need to have items/products to add!!'
        elif List.objects.filter(name=postData['name']).exists():
            errors['name']='This item/product already added!'
        elif len(postData['name'])>255:
            errors['name']='Your item that youe trying to add, have to have less than 255 character!'
        else:
            
            List.objects.create(name=postData['name'],addtolist_by=User.objects.get(id=int(postData['me'])))
            me = User.objects.get(id=int(postData['me']))
            item = List.objects.get(name=postData['name'])
            me.added.add(item)
            errors['success']="successfully!"
           
        return errors
class List(models.Model):
    name= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ManyToManyField(User,related_name='added') 
    addtolist_by = models.ForeignKey(User,related_name='addedtolist')
    objects = ListManager() 



