from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) == 0:
            errors["full_name"] = "your first name should be field"
        if len(postData['last_name']) == 0:
            errors["last_name"] = "your last name should be field"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "email invalid"
        if User.objects.filter(email=postData['email']).exists():
            errors['email_registrationn']='This email already exists!'
        if len(postData['password'])<6:
            errors['password']='Your password need to be more than 6 character!'
        if postData['password']!=postData['password_comfirm']:
            errors['password_match']='Password Comfirm need to be match with your password!!'
        if len(errors)==0:
            password_hash = bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt())         
            User.objects.create(first_name=postData['first_name'],last_name = postData['last_name'],email=postData['email'],password=password_hash)
        return errors 
    def login_validator(self,postData):
        errors={}
        if User.objects.filter(email=postData['email']).exists():
            user=User.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password_match']="Email and/or Password incorect!"
        else:
            errors['password_match']="Email and/or Password incorect!"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)   
    last_name = models.CharField(max_length=255)   
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 
    def __repr__(self):
        return "<User :  {} {} , {}>".format( self.first_name,self.last_name,  self.email)