from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count, Q


# Create your models here.
class Product(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    start_course = models.DateTimeField(blank=True, null=True)
    max_student = models.IntegerField(validators=[MinValueValidator(1)],)
    min_student = models.IntegerField(validators=[MinValueValidator(1)],)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)],)

    def __str__(self):
        return f'{self.author} {self.title}'


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=250)
    link = models.URLField(max_length=250)

    def __str__(self):
        return f'{self.product} {self.title}'


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    student = models.ManyToManyField(get_user_model(), blank=True)
    def __str__(self):
        return f'{self.product} {self.student}'


class Access_Product(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Группа заполняется с учетом минимальной заполненности
        Если есть несколько групп, то сперва все они заполнятся до
        минимального уровня, по одной записи, равномерно
        Затем будет равномерное распределение между группами
        """
        super().save(*args, **kwargs)
        query = Q(ct_students__lt=self.product.min_student)

        group_query = self.product.group_set.all().annotate(
            ct_students=Count('student')).filter(query).order_by('id')
        if group_query:
            min_group = group_query[0]
        else:
            try:
                query = Q(ct_students__lt=self.product.max_student)
                min_group = self.product.group_set.all().annotate(
                ct_students=Count('student')).filter(query).order_by('ct_students')[0]
            except IndexError():
                raise IndexError('Все места забиты')

            group = Group.objects.get(pk=min_group.pk)
            group.product = self.product
            group.student.add(self.user)
            group.save()
