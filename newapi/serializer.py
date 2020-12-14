from rest_framework import serializers
from news.models import Newsmodel, Comment, cartegory



class Newsserializer(serializers.ModelSerializer):
    class Meta:
        model= Newsmodel
        fields= '__all__'


class Cartegoryserializer(serializers.ModelSerializer):
    class Meta:
        model= cartegory
        fields= '__all__'

class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields= '__all__'






