from django.db import models

# Create your models here.

class LandInfo(models.Model):
    title = models.CharField(max_length=300, null=True)
    location = models.CharField(max_length=300, null=True)
    traffic = models.CharField(max_length=300, null=True)
    ldarea_low_lim = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    ldarea_cap = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_low_lim = models.IntegerField(default=0, null=True)
    price_ceil = models.IntegerField(default=0, null=True)
    buildcove = models.CharField(max_length=50, null=True)
    geography = models.CharField(max_length=50, null=True)
    usage_area = models.CharField(max_length=50, null=True)
    cont_add = models.CharField(max_length=200, null=True)
    cont_num = models.CharField(max_length=200, null=True)
    url = models.URLField(max_length=300)
