from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    # name, price, image, release_date, lte_exists и slug
    name = models.CharField(max_length=256, null=False)
    price = models.FloatField()
    image = models.CharField(max_length=256)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

