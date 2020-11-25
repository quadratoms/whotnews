from django import forms
from .models import Article, Profile


class ArticleForm (forms. ModelForm ):
	class Meta :
		model = Article
		fields = [ 'article_cat','heading','article_img','article_body' ]
	
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ['user']




