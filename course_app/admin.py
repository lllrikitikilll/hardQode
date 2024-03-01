from django.contrib import admin
from course_app.models import Product, Lesson, Group, Access_Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'max_student', 'min_student', 'price']
    list_display_links = ['title', 'author',]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'product']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'count_student']

    def count_student(self, obj):
        return obj.student.count()


@admin.register(Access_Product)
class Access_ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']
    list_display_links = ['id', 'user', 'product']

