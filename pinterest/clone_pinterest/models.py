from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Press(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    date=models.DateField()
    image=models.ImageField(upload_to='press')

    def __str__(self):
        return self.title
    
class News(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    date=models.DateField()
    image=models.ImageField(upload_to='press')

    def __str__(self):
        return self.title

class Board(models.Model):
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    private=models.BooleanField(null=True,blank=True)
    image1=models.ImageField(upload_to='board',null=True,blank=True)
    image2=models.ImageField(upload_to='board',null=True,blank=True)
    image3=models.ImageField(upload_to='board',null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Pin(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='product')
    board=models.ForeignKey(Board,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    url=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profilepic')
    profilename=models.CharField(max_length=30,null=True,blank=True)

    
    def __str__(self):
        return str(self.user)
    
class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    pin=models.ForeignKey(Pin,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pin)
    

class SavedPin(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='savedpins')
    board=models.ForeignKey(Board,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    url=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title
    

class Update(models.Model):
    title=models.CharField(max_length=300)
    update=models.TextField(null=True,blank=True)
    image1=models.ImageField(upload_to='updates',null=True,blank=True)
    image2=models.ImageField(upload_to='updates',null=True,blank=True)
    image3=models.ImageField(upload_to='updates',null=True,blank=True)
    

    def __str__(self):
        return self.title
    

class Message(models.Model):
    title=models.CharField(max_length=300,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    image1=models.ImageField(upload_to='msgs',null=True,blank=True)
 
    

    def __str__(self):
        return self.title