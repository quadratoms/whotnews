from django import forms
from .models import Comment, Newsmodel, cartegory


class CommentForm (forms.ModelForm ):
	class Meta :
		model = Comment
		fields = ['body']
	

a=cartegory.objects.all()
class linkform(forms.Form):
    
	link=forms.CharField(max_length=200, required=True)
	cat= forms.ModelMultipleChoiceField(a)


class NewsmodelForm(forms.ModelForm):
	class Meta:
		model = Newsmodel
		fields = '__all__'
	





