from rest_framework import serializers
from .models import Restaurant

class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name','describtion','opening_time','closing_time','logo']