from django.db import models

# Create your models here.
class userdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    password=models.CharField(max_length=264)

    def __str__(self):
        return self.email

class actordetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    password=models.CharField(max_length=264)
    name=models.CharField(max_length=264)
    passport=models.CharField(max_length=264)
    profilepic=models.ImageField(upload_to='profile_pics')
    dob=models.CharField(max_length=264)
    age=models.CharField(max_length=264)
    mobile=models.CharField(max_length=264)
    gender=models.CharField(max_length=264)
    address=models.CharField(max_length=264)
    city=models.CharField(max_length=264)
    pin=models.CharField(max_length=264)
    state=models.CharField(max_length=264)
    country=models.CharField(max_length=264)
    webseries=models.CharField(max_length=264)
    serial=models.CharField(max_length=264)
    movies=models.CharField(max_length=264)
    shortmovies=models.CharField(max_length=264)
    experience=models.CharField(max_length=264)
    haircolor=models.CharField(max_length=264)
    skincolor=models.CharField(max_length=264)
    def __str__(self):
        return self.email

class modeldetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    password=models.CharField(max_length=264)
    name=models.CharField(max_length=264)
    passport=models.CharField(max_length=264)
    profilepic=models.ImageField(upload_to='profile_pics')
    dob=models.CharField(max_length=264)
    age=models.CharField(max_length=264)
    mobile=models.CharField(max_length=264)
    gender=models.CharField(max_length=264)
    address=models.CharField(max_length=264)
    city=models.CharField(max_length=264)
    pin=models.CharField(max_length=264)
    state=models.CharField(max_length=264)
    country=models.CharField(max_length=264)
    catalog=models.CharField(max_length=264)
    hoarding=models.CharField(max_length=264)
    mrmrs=models.CharField(max_length=264)
    des_rmp=models.CharField(max_length=264)
    experience=models.CharField(max_length=264)
    haircolor=models.CharField(max_length=264)
    skincolor=models.CharField(max_length=264)
    def __str__(self):
        return self.email

class dancerdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    password=models.CharField(max_length=264)
    name=models.CharField(max_length=264)
    passport=models.CharField(max_length=264)
    profilepic=models.ImageField(upload_to='profile_pics')
    dob=models.CharField(max_length=264)
    age=models.CharField(max_length=264)
    mobile=models.CharField(max_length=264)
    gender=models.CharField(max_length=264)
    address=models.CharField(max_length=264)
    city=models.CharField(max_length=264)
    pin=models.CharField(max_length=264)
    state=models.CharField(max_length=264)
    country=models.CharField(max_length=264)
    barathanatyam=models.CharField(max_length=264)
    freestyle=models.CharField(max_length=264)
    sidedancer=models.CharField(max_length=264)
    danceshow=models.CharField(max_length=264)
    experience=models.CharField(max_length=264)
    haircolor=models.CharField(max_length=264)
    skincolor=models.CharField(max_length=264)
    def __str__(self):
        return self.email

class singerdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    password=models.CharField(max_length=264)
    name=models.CharField(max_length=264)
    passport=models.CharField(max_length=264)
    profilepic=models.ImageField(upload_to='profile_pics')
    dob=models.CharField(max_length=264)
    age=models.CharField(max_length=264)
    mobile=models.CharField(max_length=264)
    gender=models.CharField(max_length=264)
    address=models.CharField(max_length=264)
    city=models.CharField(max_length=264)
    pin=models.CharField(max_length=264)
    state=models.CharField(max_length=264)
    country=models.CharField(max_length=264)
    movie=models.CharField(max_length=264)
    serial=models.CharField(max_length=264)
    experience=models.CharField(max_length=264)
    haircolor=models.CharField(max_length=264)
    skincolor=models.CharField(max_length=264)
    def __str__(self):
        return self.email

class consultdetail(models.Model):
    email=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    cmpname=models.CharField(max_length=264)
    password=models.CharField(max_length=264)
    mobile=models.CharField(max_length=264)
    address=models.CharField(max_length=264)
    city=models.CharField(max_length=264)
    pin=models.CharField(max_length=264)
    state=models.CharField(max_length=264)
    country=models.CharField(max_length=264)

    def __str__(self):
        return self.email

class counter(models.Model):
    iid=models.CharField(max_length=264)
    def __str__(self):
        return self.iid

class createactord(models.Model):
    email=models.CharField(max_length=264)
    aid=models.CharField(max_length=264)
    name=models.CharField(max_length=264)
    desc=models.CharField(max_length=264)
    webseries=models.CharField(max_length=264)
    serial=models.CharField(max_length=264)
    movies=models.CharField(max_length=264)
    shortmovies=models.CharField(max_length=264)
    def __str__(self):
        return self.aid

class createmodeld(models.Model):
    email=models.CharField(max_length=264)
    aid=models.CharField(max_length=264)
    name=models.CharField(max_length=264)
    desc=models.CharField(max_length=264)
    catalog=models.CharField(max_length=264)
    hoarding=models.CharField(max_length=264)
    mrmrs=models.CharField(max_length=264)
    des_rmp=models.CharField(max_length=264)
    def __str__(self):
        return self.aid

class createdancerd(models.Model):
    email=models.CharField(max_length=264)
    aid=models.CharField(max_length=264)
    name=models.CharField(max_length=264)
    desc=models.CharField(max_length=264)
    barathanatyam=models.CharField(max_length=264)
    freestyle=models.CharField(max_length=264)
    sidedancer=models.CharField(max_length=264)
    danceshow=models.CharField(max_length=264)
    def __str__(self):
        return self.aid

class createsingerd(models.Model):
    email=models.CharField(max_length=264)
    aid=models.CharField(max_length=264)
    name=models.CharField(max_length=264)
    desc=models.CharField(max_length=264)
    serial=models.CharField(max_length=264)
    movie=models.CharField(max_length=264)
    def __str__(self):
        return self.aid

class enrolled(models.Model):
    email=models.CharField(max_length=264)
    aid=models.CharField(max_length=264)
    files=models.FileField(upload_to='')
    def __str__(self):
        return self.aid
