from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    
    def createUser(self, postData):
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        self.create(name = postData['name'], alias = postData['alias'], email = postData['email'], password = password)

    def loginVal(self, postData):
        results = {'errors': [], 'status': False, 'user': None}
        email_matches = self.filter(email = postData['email'])
        if len(email_matches) == 0:
            results['errors'].append('Please check email and password and try again.')
            results['status'] = True
        else:
            results['user'] = email_matches[0]
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Please check email and password and try again.')
                results['status'] = True
            return results

    def registerVal(self, postData):
        results = {'errors': [], 'status': False}

        if len(postData['name']) < 2:
            results['status'] = True
            results['errors'].append(' Name is too short.')

        if len(postData['alias']) < 2:
            results['status'] = True
            results['errors'].append('Alias is too short')

        if not re.match(r'[^@]+@[^@]+\.[^@]+', postData['email']):
            results['status'] = True
            results['errors'].append('Password is not valid')

        if len(postData['password']) < 8:
            results['status'] = True
            results['errors'].append('Password must be 8 chars')

        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Passwords do not match')

        user = self.filter(email = postData ['email'])
        
        if len(user) > 0:
            results['status'] = True
            results['errors'].append('Email already exists')

        return results










class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
