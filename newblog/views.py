from random import *
from .models import Article, Profile, cartegory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import ArticleForm, ProfileForm


from django . core . mail import send_mail , BadHeaderError
from django . http import HttpResponse
from django . contrib. auth . forms import PasswordResetForm
from django . template. loader import render_to_string
from django . db . models . query_utils import Q
from django . utils . http import urlsafe_base64_encode
from django . contrib. auth . tokens import default_token_generator
from django . utils . encoding import force_bytes

def p(request):
	p=Profile.objects.all()
	p=list(p)
	r=sample(p, 3)
	return r

def register(request):
	r=p(request)
	user_login(request)
	
	if 'btnreg' in request.POST:
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cp = request.POST['passwordc']
		
		if User.objects.filter(username=username).exists():
			messages.info(request,'username taken')
			
			return redirect('/whot/register')
		
		elif User.objects.filter(email=email).exists():
			messages.info(request, 'email taken')
			return redirect('/whot/register')
		else:
			if password==cp:
				user = User.objects.create_user(username,email=email,password=password,first_name=first_name,last_name=last_name)
				user.save()
				user = auth.authenticate(request, username=username, password=password)
				auth.login(request, user)
				return redirect('/whot/')
			else:
				messages.info(request, 'password not match')
			return redirect('/whot/register')
	return render(request, 't/register.html', {'r':r})
			
def edit_profile(request):
	r=p(request)
	a=request.user
	b=Profile.objects.get(user=a)
	if 'btnprof' in request.POST:
		
		print(a)
		form = ProfileForm(request. POST, instance=b)
		if form. is_valid ():
			print()
			form. save ()
			print('save')
			messages.info(request, 'profile saved')
			return redirect('/whot/')
	else:
		print(request.user, ' you')
		
		form = ProfileForm (instance=b)
		
	return render(request, 't/edit_profile.html', {'form':form, 'r':r})

def user_login(request):
    if 'btnsubmit' in request.POST:
        print('hello')
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        print(username,' ', password)
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print('correct')
            auth.login(request, user)
            print('log')
            return redirect('/whot/')
        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('/whot/')


def user_logout(request):
    auth.logout(request)
    return redirect('whot/')

'''def gethelp(request):

    if request.method == 'POST':
        adviser= request.POST.get('adviser')
        advise = request.POST.get('advise')

        help = HelpMe()
        help.adviser=adviser
        help.advise=advise
        help.save()
    else:
        pass'''

def home(request):
    r=p(request)
    user_login(request)
    story = Article.objects.all()
    randoms=choice(story)
    #gethelp(request)
    return render(request, 't/bloghome.html', {'story': story, 'randoms':randoms, 'r':r})


def article(request, id):
    r=p(request)
    user_login(request)
    story = Article.objects.get(id=id)
    story.view += 1
    story.save()
    #'gethelp(request)

    return render(request, 't/article.html', {'story': story, 'r':r})

def cat(request, id):
    r=p(request)
    
    user_login(request)
    storys = cartegory.objects.get(id=id)
    story= Article.objects.filter(article_cat=storys)
    #'gethelp(request)

    return render(request, 't/article_cat.html', {'story': story, 'storys':storys, 'r':r})

def create_or_edit_post (request, id =None ):
	r=p(request)
	post = Article.objects.get(id=id) if id else None
	form = ArticleForm(request. POST, instance=post)
	print(post)
	if request.method == "POST" :
		
		
		if form. is_valid ():
			
			a=form.save()
			a.author=request.user
			a.save()
			
			return redirect('/whot')
	else:
		form = ArticleForm (instance = post)
	
	return render(request, "t/edit_article.html", {'form':form})

def profile(request, id):
	r=p(request)
	profile=Profile.objects.get(id=id)
	userprof=User.objects.get(username=profile.user)
	
	
	return render(request, 't/profile.html', {'profile':profile, 'userprof':userprof, 'r':r})

'''def create_or_edit_post (request, id =None ):
	post = get_object_or_404 ( Article , id = id) if id else None
	if request.method == "POST" :
		form = ArticleForm(request. POST)
		if form. is_valid ():
			post = form. save ()
			return redirect(post_detail, post.id)
		else:
			form = ArticleForm (instance = post)
	
	return render(request, "Article.html", {'form':form})'''

def password_reset_request ( request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm ( request. POST )
		if password_reset_form . is_valid ():
			print('valid')
			data = password_reset_form . cleaned_data [ 'email' ]
			associated_users = User . objects. filter ( Q ( email = data ))
			if associated_users . exists ():
				print('exidt')
				for user in associated_users :
					subject = "Password Reset Requested"
					email_template_name = "p.txt"
					c = {
					"email" : user . email ,
					'domain' : '127.0.0.1:8000' ,
					'site_name' : 'Whot' ,
					"uid" : urlsafe_base64_encode ( force_bytes ( user . pk )),
					"user" : user ,
					'token' : default_token_generator . make_token ( user ),
					'protocol' : 'http' ,
					}
					email = render_to_string ( email_template_name , c )
					print('ready/')
					try :
						send_mail ( subject , email , 'admin@whot.com' , [ user . email ], fail_silently = False )
						print('sent')
					except BadHeaderError :
						return HttpResponse ( 'Invalid header found.' )
					return redirect ( "/password_reset/done/" )
	password_reset_form = PasswordResetForm ()
	print(345)
	return render ( request= request, template_name = "resetp.html" , context = { "password_reset_form" : password_reset_form })
# Create your views here.