from django.shortcuts import render
from django.http import JsonResponse
from .models import Restaurant
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ResturantSerializer


class ResturantList(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = ResturantSerializer


def restaurant_list(request):
	my_resturant = []
	for rest in Restaurant.objects.all():
		my_resturant.append({
				'Name: ': rest.name,
				'Description': rest.describtion,
				'opening time': rest.opening_time,
				'closing_time': rest.closing_time
		})
	return JsonResponse(my_resturant,safe =False)

def restaurant_detail(request, rest_id):
	rest_obj = Restaurant.objects.get(id=rest_id)
	my_rest = {
			'Name:':rest_obj.name,
			'Desc:':rest_obj.describtion,
			'opening time:':rest_obj.opening_time,
			'closing time:':rest_obj.closing_time,
	}
	return JsonResponse(my_rest,safe =False)