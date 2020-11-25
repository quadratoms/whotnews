from django import forms
from .models import Comment, Newsmodel


class CommentForm (forms.ModelForm ):
	class Meta :
		model = Comment
		fields = ['body']
	


class linkform(forms.Form):
	link=forms.CharField(max_length=200, required=True)


class NewsmodelForm(forms.ModelForm):
	class Meta:
		model = Newsmodel
		fields = '__all__'
	





