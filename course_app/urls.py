from django.urls import path
from course_app.views import products, user_lessons, statistics

app_name = 'course_app'

urlpatterns = [
    path('courses', products, name='products'),
    path('lessons/<str:product>', user_lessons, name='user_lessons'),
    path('statistics', statistics, name='statistic'),
]