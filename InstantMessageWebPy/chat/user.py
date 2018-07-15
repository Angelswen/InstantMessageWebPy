from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    status = models.IntegerField(max_length=5)
    auth = models.IntegerField(max_length=5)
    loginTime = models.DateTimeField()
    createTime = models.DateTimeField()
    logoutTime = models.DateTimeField()




