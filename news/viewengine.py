from .models import Newsmodel, Comment, cartegory
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta
from newspaper import Article

def searchengine(keywords):
    newslist=[]
    a = Newsmodel.objects.all().order_by('-date')
    for each in a:
        if keywords in each.heading or keywords in each.content:
            newslist.append(each)
    if len(newslist) > 0:
        return newslist
    else:
        return None


def topstory():
    b=[]
    a = Newsmodel.objects.filter(date__range=[date.today()+timedelta(days=-10), date.today()+timedelta(days=1)]).order_by('-view')
    if len(a) > 3:
        for i in range(3):
            b.append(a[i])
        
        return b
    else:
        return a

def catmake(cat, num=None):
    ''' this will return a list of num amout of items in cat moddel
    order by recent
    if num is None it return all
    num is an itergal;;;\''''
    
    b=[]
    a = cartegory.objects.get(cat=cat)
    n=Newsmodel.objects.filter(newscat=a).order_by('-date')
    if num==None:
        return n
    else:
        
        if len(n) != 0:
            if len(n) < num:
                for i in range(len(n)):
                    b.append(n[i])
                return b
            else:
                for i in range(num):
                    b.append(n[i])
                return b
        else:
            print('empty catergory')
            pass


def catlistlist(l, num=3):
    '''
    collect a list of cartergory name and return num amount of each cartegory
    e.i a list of the catergory with list of each cat model
    '''
    a=[]
    if l != None:
        for i in l:
            
            try:
                print(i)
                a.append(catmake(i, num))
                print(a)
            except:
                print('write the right cartegory name')
        return a
    else:
        print('l is a list of cartegory name')
        pass



'''					n = Newsmodel()
					n.author=article.authors
					n.article_img=article.top_img
					n.heading=article.title
					n.content=article.article_html
					n.source_url=each

					n.save()
'''



def converttonews(link):

    
    article = Article(link)
    article.download()
    article.parse()
    l=['vanguard', 'nation', 'cnn', 'theguardian', '127', 'dailytimes', 'dailytrust', 'tribune']
    source=None#  this may bring error, idont know
    for s in l:
        if s in link:
            source= s
            break
        else:
            pass

    return {
            'source': source+'.png',
            'source_url':link,
            'heading': article.title,
            'article_img': article.top_img,
            'content': article.text
        }
    
    

def addhtml(text):

    a= '<p>'+text+'</p>'
    a= a.replace('Kindly Share This Story', '')
    a= a.replace('\n', '</p>\n<p>')

    return a


