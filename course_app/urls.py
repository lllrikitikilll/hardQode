from django.urls import path
from course_app.views import get_products
app_name = 'course_app'

urlpatterns = [
    path('courses', get_products, name='get_products'),
    path('lessons'),
]