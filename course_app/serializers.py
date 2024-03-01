from django.contrib.auth import get_user_model
from rest_framework import serializers



class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    title = serializers.CharField(max_length=250)
    price = serializers.DecimalField(decimal_places=2, max_digits=7, min_value=0)
    max_student = serializers.IntegerField(min_value=1)
    start_course = serializers.DateTimeField(allow_null=True, required=False)
    min_student = serializers.IntegerField(min_value=1)
    count_lessons = serializers.IntegerField(min_value=0)


