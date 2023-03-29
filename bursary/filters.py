import django_filters
from django_filters import DateFilter
from .models import *

class ApplicationFilter(django_filters.FilterSet):
    class Meta:
        model = Applications
        fields = '__all__'
        exclude =['student','date_created']