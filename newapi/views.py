from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import Newsmodel, Comment, cartegory
from news.viewengine import searchengine, topstory
from .serializer import Newsserializer, Commentserializer, Cartegoryserializer



@api_view(['GET'])
def allnews(request):
    
    newslist= Newsmodel.objects.all()
    serialize= Newsserializer(newslist, many=True)
    
    return Response(serialize.data)



@api_view(['GET'])
def news(request, id):
    
    newscontent= Newsmodel.objects.get(id=id)
    newscontent.view += 1
    newscontent.save()
    serialize= Newsserializer(newscontent)
    
    return Response(serialize.data)



@api_view(['GET', 'POST'])
def comment(request, id):
    if  request.method=='GET':
        newscontent= Newsmodel.objects.get(id=id)
        newscomment= newscontent.comment_set.all().order_by('-time')
        serialize= Commentserializer(newscomment, many=True)
    if request.method=='POST':
        serialize= Commentserializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
    
    return Response(serialize.data)


@api_view(['GET'])
def newscat(request, id):
    
    newscat= cartegory.objects.get(id=id)
    cats= Newsmodel.objects.filter(newscat=newscat.id)
    serialize= Newsserializer(cats, many=True)
    
    return Response(serialize.data)



@api_view(['GET'])
def catlist(request):
    
    cats= cartegory.objects.all()
    serialize= Cartegoryserializer(cats, many=True)
    
    return Response(serialize.data)



@api_view(['GET'])
def search(request, pk):
    
    news= searchengine(pk)
    serialize= Newsserializer(news, many=True)
    
    return Response(serialize.data)



@api_view(['GET'])
def top(request):
    
    news= topstory()
    serialize= Newsserializer(news, many=True)
    
    return Response(serialize.data)


'''
newsposter will be add later 
it will take two pk, first will be str which is url 
and the other will be slug which will category

'''
# Create your views here.

