from django.db import models

class contact(models.Model):
    name=models.CharField(null=True,max_length=50)
    email=models.CharField(null=True,max_length=50)
    phone=models.CharField(null=True,max_length=50)
    message=models.CharField(null=True,max_length=50)

    def __str__(self):
        return str(self.id)

class feedback(models.Model):
    name=models.CharField(null=True,max_length=50)
    message=models.CharField(null=True,max_length=50)
    def __str__(self):
        return str(self.id)
    
class foodbook(models.Model):
    name=models.CharField(null=True,max_length=50)
    date=models.DateField()
    RegNo=models.CharField(null=True,max_length=50)
    def __str__(self):
        return str(self.id)

# Create your models here.
