from medicSearch.models import *
from medicSearch.models.DayWeek import DayWeek
from medicSearch.models.Neighborhood import Neighborhood

class Address(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, null=True, related_name='neighborhood', on_delete=models.SET_NULL)
    name = models.CharField(null=False, max_length=100)
    address = models.CharField(null=False, max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    days_week = models.ManyToManyField(DayWeek, related_name='days_week')
    phone = models.CharField(null=True, max_length=50, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)