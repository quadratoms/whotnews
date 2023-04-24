from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField


class cartegory(models.Model):
	catlist='News Polictics World Religion Education Fashion Technology Entertainment Medical Sport'
	CAT=models.TextChoices('CAT', catlist)
	cat=models.CharField(choices=CAT.choices, max_length=15)
	
	def __str__(self):
		return self.cat





class Newsmodel(models.Model):
    newscat=models.ManyToManyField(cartegory)
    source=models.CharField(blank=True, null=True, max_length=20)
    author=models.CharField(blank=True, null=True, max_length=20)
    source_url= models.CharField(blank=True, null=True, max_length=1000)
    heading = models.CharField(max_length=300, unique=True)
    date=models.DateTimeField(auto_now_add=True)
    article_img=models.CharField(max_length=200, blank=True)
    content=RichTextField(blank=True, null=True)
    view=models.IntegerField(default=0)
    post=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.heading


class Comment(models.Model):
    comment = models.ForeignKey(Newsmodel, on_delete=models.CASCADE)
    us = models.ForeignKey("auth.User",null= True, blank= True, on_delete=models.SET_NULL)
    body = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body



# Create your models here.
