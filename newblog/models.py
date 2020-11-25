from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField
#from django_currentuser.db.models import CurrentUserField



class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, null=True)
	age = models.DateField(blank=True, null=True)
	profession = models.CharField(max_length=10, null=True)
	telephone= models.IntegerField(default='0', blank=True, null=True)
	profile_pic=models.ImageField(blank=True, null=True)
	about=models.TextField(blank=True, null=True)
	
	def __str__(self):
		return self.name


class cartegory(models.Model):
	catlist='Religion Culture Education Fashion Technology Art&music Cooking Entertainment Garden Health&Fittness History Kid Medical Parenting Romance Sport'
	CAT=models.TextChoices('CAT', catlist)
	cat=models.CharField(choices=CAT.choices, max_length=15)
	
	def __str__(self):
		return self.cat


class Article(models.Model):
	
	article_cat=models.ForeignKey(cartegory,on_delete=models.PROTECT)
	author=models.ForeignKey("auth.User",null= True, blank= True, on_delete=models.SET_NULL)# shoulldbechanged
	heading = models.CharField(max_length=300)
	date=models.DateTimeField(auto_now_add=True)
	article_img=models.ImageField(upload_to= 'article_image', blank=True)
	article_body=RichTextField(blank=True, null=True)
	view=models.IntegerField(default=0)
	def __str__(self):
		return self.heading


# Create your models here.
