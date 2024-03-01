from django.db.models import Count
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from course_app.models import Product
from course_app.serializers import ProductSerializer


# Create your views here.

@api_view(['GET'])
def get_products(request):
    dct = {}
    products = Product.objects.all().annotate(
        count_lessons=Count('lessons')).select_related()
    for i in products:
        dct = {
            'id': i,
            'author': i,
            'title': i,
            'start_course': i,
            'max_student': i,
            'min_student': i,
            'price': i,
            'lessons': i
        }
    print(dct)
    serializer = ProductSerializer(data=products, many=True)
    print(serializer.is_valid())
    print(serializer.data)
    return Response(serializer.data)
