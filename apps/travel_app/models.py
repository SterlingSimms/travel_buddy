from __future__ import unicode_literals

from django.db import models

class TripManager(models.Manager):
    def basic_validation(self, postData):
        errors = {}
        now = datetime.datetime.now()
        later = now + datetime.timedelta(days = 1)

        if len(POSTdata['name']) < 3:
            errors['name'] = "Name should be at least 3 characters."
        if len(POSTdata['username']) < 3:
            errors['username'] = "Username should be at least 3 characters."
        if len(POSTdata['password']) < 6:
            errors['password'] = "Password should be at least 6 characters."
        if len(POSTdata['confirm_password']) != POSTdata['password']:
            errors['confirm_password'] = "Passwords do not match."
        if len(POSTdata['destination']) < 1:
            errors['empty'] = "Please complete all fields."
        if len(POSTdata['description']) < 1:
            errors['empty'] = "Please complete all fields."
        if len(POSTdata['travel_from']) < 1:
            errors['empty'] = "Please complete all fields."
        if len(POSTdata['travel_to']) < 1:
            errors['empty'] = "Please complete all fields."
        if now(POSTdata['travel_from']) >= later:
            errors['later'] = "All traveling plans must be made at least 1 day in advance."
        if now(POSTdata['travel_to']) >= later:
            errors['later'] = "All traveling plans must be made at least 1 day in advance."
        if now(POSTdata['travel_to']) < now(POSTdata['travel_from']):
            errors['invalid'] = "Invalid date selections."
        return errors

class User(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Travel(models.Model):
    destination = models.CharField(max_length = 255)
    desc = models.TextField()
    travel_from = models.CharField(max_length = 255)
    travel_to = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    users = models.ManyToManyField(User, related_name="join")