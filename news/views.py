from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import CommentForm, linkform, NewsmodelForm
from .viewengine import searchengine, topstory, catmake, addhtml, catlistlist, converttonews, idk
from .models import Newsmodel, Comment, cartegory
from django.contrib import messages

import pyttsx3
from django.http import HttpResponse
from tempfile import TemporaryFile
from gtts.tts import gTTS

def tts(request):
    text = request.GET.get('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150) # Set the speaking rate
    engine.setProperty('voice', voices[1].id) # Set the voice
    engine.save_to_file(text, 'audio.mp3') # Generate the TTS audio file
    engine.runAndWait()
    with open('audio.mp3', 'rb') as f:
        response = HttpResponse(f.read(), content_type='audio/mpeg')
        response['Content-Disposition'] = 'attachment; filename=tts_audio.mp3'
        return response
    # tts = gTTS(text=text, lang='en-us', slow=False) # Generate TTS audio file
    # response = HttpResponse(tts.stream(), content_type='audio/mpeg')
    # response['Content-Disposition'] = 'attachment; filename=tts_audio.mp3'
    # return response


def home(request):
    top=topstory()
    #l= ['Polictics', 'Education', 'Sport','World']
    #c=catlistlist(l, num=2)
    
    c=idk()
    
    if 'search' in request.POST:
        print(22)
        keywords = request.POST.get('keywords')
        a='/search='+ keywords + '/'
        return redirect(a)
    catlink=cartegory.objects.all()
    allnews = Newsmodel.objects.all().order_by('-date')
    p=Paginator(allnews, 15)
    pnum= request.GET.get('page', 1)
    allnews = p.get_page(pnum)
    context={
        'allnews':allnews,
        'top':top ,
        #'first':first,
        #'second':second,
        #'third':third,
        #'fourth':fourth,
        'c':c,
        'catlink':catlink

    }


    return render(request, 'home.html', context)


def news(request, id):
    
    if 'search' in request.POST:
        print(22)
        keywords = request.POST.get('keywords')
        a='/search='+ keywords + '/'
        return redirect(a)
    
    c=idk()
    newscontent= Newsmodel.objects.get(id=id)
    newscontent.view +=1
    newscontent.save()
    a= newscontent.content
    a=a.replace('\n', ' ')
    a=a.replace('  ', ' ')
    a=a.replace('   ', ' ')
    a=a.replace('    ', ' ')
    
    newscontent.content = addhtml(newscontent.content)
    newscomment= newscontent.comment_set.all().order_by('-time')
    
    catlink=cartegory.objects.all()

    if 'comment' in request.POST:
        body = request.POST.get('body')
        if body != '':
            print(body)
            
            comment= Comment(comment=newscontent,us=request.user, body=body)
            
            comment.save()
        return redirect(request.path)

    return render(request, 'news.html', {'a':a, 'c':c,'catlink':catlink, 'newscontent':newscontent, 'newscomment':newscomment})


def newscat(request, id):
    if 'search' in request.POST:
        print(22)
        keywords = request.POST.get('keywords')
        a='/search='+ keywords + '/'
        return redirect(a)
    c=idk()
    newscat= cartegory.objects.get(id=id)
    cats= Newsmodel.objects.filter(newscat=newscat.id)
    p=Paginator(cats, 20)
    pnum= request.GET.get('page', 1)
    catlist = p.get_page(pnum)
    catlist.name=newscat#instance value for catlist
    print(newscat)
    print(catlist)
    catlink=cartegory.objects.all()
    


    return render(request, 'newscat.html', {'c':c,'catlink':catlink, 'catlist':catlist})

def search(request, pk):
    if 'search' in request.POST:
        print(22)
        keywords = request.POST.get('keywords')
        a='/search='+ keywords + '/'
        return redirect(a)
    news=searchengine(pk)
    p=Paginator(news, 15)
    pnum= request.GET.get('page', 1)
    try:
        newslist = p.get_page(pnum)
    except:# in case there is no result for search
        newslist = None
    catlink=cartegory.objects.all()

	
    return render(request, 'search.html', {'catlink':catlink, 'newslist':newslist})

def allpost(request):
    if 'search' in request.POST:
        print(22)
        keywords = request.POST.get('keywords')
        a='/search='+ keywords + '/'
        return redirect(a)

    alln = Newsmodel.objects.all().order_by('-date')
    p=Paginator(alln, 10)
    pnum= request.GET.get('page', 1)
    allnews = p.get_page(pnum)
    catlink=cartegory.objects.all()



    return render(request, 'allpost.html', {'catlink':catlink, 'allnews':allnews})





def newsposter(request):
    form= linkform(request.POST)


    if 'convert' in request.POST:
        form= linkform(request.POST)
        if form.is_valid():

            link=request.POST.get('link')
            cat= form.cleaned_data.get('cat')
            
            
        
            try:
                a=converttonews(link)
                c=Newsmodel()
                c.source= a['source']
                c.source_url= a['source_url']
                c.heading= a['heading']
                c.article_img= a['article_img']
                c.content= a['content']
                c.save()
                
                c.newscat.add(*cat)
                c.save()
                
                messages.success(request, 'created, it will be posted soon')
            except:
                print(567)
                messages.error(request, 'link can\'t be convert or check the link')
        return redirect('/newsposter/')
        

    return render(request, 'newsposter.html', {'form':form})








# Create your views here.



