from django.db import models
from datetime import datetime, timedelta

import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z -]+$')
        LAST_NAME_REGEX = re.compile(r'^[a-zA-Z -]+$')
        MIN_AGE = 365*13
        today = datetime.now()

        if post_data['birthday'] != '':
            birthday = datetime.strptime(post_data['birthday'], "%Y-%m-%d")


        if len(post_data['first_name']) < 2:
            errors['first_name'] = 'First name should have at least 2 characters.'
        elif not FIRST_NAME_REGEX.match(post_data['first_name']):
            errors['first_name'] = 'First name must consist of only letters'
        
        if len(post_data['last_name']) < 2:
            errors['last_name'] = 'Last name should have at least 2 characters.'
        elif not LAST_NAME_REGEX.match(post_data['last_name']):
            errors['last_name'] = 'Last name must consist of only letters and space or dash characters'

        
        if post_data['birthday'] == '':
            errors["birthday"] = "Please select a birthday"
        elif birthday > today - timedelta(days=MIN_AGE):
            errors["birthday"] = "You must be at least 13 years old to register"
        elif birthday >= today:
            errors["birthday"] = "Your birthday must be before today"
        
        if len(post_data['email']) < 1:
            errors['email'] = 'Email is required'
        elif not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Please enter a valid email address'
        
        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if post_data['password'] != post_data['pw_confirm']:
            errors['password'] = 'Passwords must match'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64)
    birthday = models.DateField(default = None)
    email = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

class Message(models.Model):
    message_text = models.TextField()
    user = models.ForeignKey(User, related_name='messages',  on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(User, related_name='comments',  on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments',  on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
