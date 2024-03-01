
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from course_app.models import Product
from course_app.serializers import ProductSerializer, LessonSerializer
from course_app.service import product_stat


# Create your views here.

@api_view(['GET'])
def products(request):
    products = Product.objects.all().annotate(
        count_lessons=Count('lessons'))
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_lessons(request: Request, product):
    user = request.user
    if user.is_authenticated:
        lessons = user.product_set.get(title=product).lessons.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def statistics(request: Request):
    return Response(product_stat())
