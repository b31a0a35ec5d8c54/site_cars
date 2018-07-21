from django.db import models

from django.urls import reverse    


class CompanyGroup(models.Model):
    i_d = models.CharField(max_length=32, default='')
    name = models.CharField(max_length=64, default='')


class Company(models.Model):
    def __str__(self):
        return 'Company inn={} name={}'.format(self.inn, self.name)
    group = models.ForeignKey(CompanyGroup, on_delete=models.SET_NULL, null=True)
    inn = models.CharField(max_length=32, default='')
    name = models.CharField(max_length=64, default='')


class Car(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name='date created')
    i_d = models.CharField(max_length=32, verbose_name='Идентификатор', default='')
    created = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    vin = models.CharField(max_length=64, verbose_name='VIN', default='')
    model = models.CharField(max_length=64, verbose_name='Модель', default='')
    year = models.IntegerField(verbose_name='Год', default=0)
    price = models.FloatField(verbose_name='Цена', default=0.0)
    gosnomer = models.CharField(max_length=64, verbose_name='Госномер', default='')
    used = models.BooleanField(verbose_name='С пробегом', default=False)
    forloan = models.BooleanField(verbose_name='На продажу', default=False)

    def imagesurl(self):
        return '/cars/{}'.format(self.id)

    def get_absolute_url(self):
        return reverse('car_list')


class CarImage(models.Model):
    car = models.ForeignKey(Car, models.CASCADE, related_name='images')
    url = models.CharField(max_length=256)