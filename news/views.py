from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import CommentForm, linkform, NewsmodelForm
from .viewengine import searchengine, topstory, catmake, addhtml, catlistlist, converttonews
from .models import Newsmodel, Comment, cartegory, Source
from django.contrib import messages



def home(request):
    top=topstory()
    c=catlistlist(['Polictics', 'Education', 'Sport','World'], num=2)
    first=catmake('Polictics')
    second=catmake('Education')
    third=catmake('Sport')
    fourth=catmake('World')
    print(fourth)
    print(c, ' lls')
    print(len(c))
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
        'first':first,
        'second':second,
        'third':third,
        'fourth':fourth,
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
    
    newscontent= Newsmodel.objects.get(id=id)
    newscontent.content = addhtml(newscontent.content)
    newscontent.view +=1
    newscontent.save()
    newscomment= newscontent.comment_set.all().order_by('-time')
    
    catlink=cartegory.objects.all()

    if 'comment' in request.POST:
        body = request.POST.get('body')
        if body != '':
            print(body)
            
            comment= Comment(comment=newscontent,us=request.user, body=body)
            
            comment.save()

    return render(request, 'news.html', {'catlink':catlink, 'newscontent':newscontent, 'newscomment':newscomment})


def newscat(request, id):
    if 'search' in request.POST:
        print(22)
        keywords = request.POST.get('keywords')
        a='/search='+ keywords + '/'
        return redirect(a)
    newscat= cartegory.objects.get(id=id)
    cats= Newsmodel.objects.filter(newscat=newscat.id)
    p=Paginator(cats, 1)
    pnum= request.GET.get('page', 1)
    catlist = p.get_page(pnum)
    print(newscat)
    print(catlist)
    catlink=cartegory.objects.all()


    return render(request, 'newscat.html', {'catlink':catlink, 'catlist':catlist})

def search(request, pk):
    if 'search' in request.POST:
        print(22)
        keywords = request.POST.get('keywords')
        a='/search='+ keywords + '/'
        return redirect(a)
    news=searchengine(pk)
    p=Paginator(news, 3)
    pnum= request.GET.get('page', 1)
    newslist = p.get_page(pnum)
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
    form= linkform()
    g=None
    

    if 'convert' in request.POST:
        link=request.POST.get('link')
        try:
            a=converttonews(link)
            c=Newsmodel(a)
            c.save()
            print(333)
            messages.success(request, 'created, it will be posted soon')
        except:
            print(567)
            messages.error(request, 'link can\'t be convert or check the link')
        return redirect('/newsposter/')
        

    return render(request, 'newsposter.html', {'form':form, 'g':g})








# Create your views here.



