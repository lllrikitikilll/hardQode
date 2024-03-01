from django.contrib.auth import get_user_model
from django.db.models import Count, Max
from course_app.models import Product


def product_stat():
    dct={}
    User = get_user_model()
    users = User.objects.all().count()
    for i in Product.objects.all():
        count_group_in_product = i.group_set.count()

        dct[i.title] = i.group_set.all().aggregate(students=Count('student'),
                                          percent_of_group=(Max(count_group_in_product * i.max_student)))
        dct[i.title]['percent_of_group'] = int(dct[i.title]['students'] / dct[i.title]['percent_of_group'] * 100)
        dct[i.title]['purchase_percent'] = int(dct[i.title]['students'] / users * 100)

    return dct

