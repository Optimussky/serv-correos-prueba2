from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return username

class DataSystem(models.Model):
    name = models.CharField(max_length=100)
    uuid = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Notification(models.Model):
    data_system = models.ForeignKey(DataSystem, on_delete=models.CASCADE)
    #uuid = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.title
