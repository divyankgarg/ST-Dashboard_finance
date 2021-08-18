import django_filters
from django_filters import CharFilter
from .models import *

class ResourceFilter(django_filters.FilterSet):
    resource=CharFilter(field_name='resource',lookup_expr='icontains',label='Resource')
    class Meta:
        model = Resources
        fields= '__all__'

class UserFilter(django_filters.FilterSet):
    # resource=CharFilter(field_name='givenname',lookup_expr='icontains',label='Name')
    class Meta:
        model = Users
        fields= '__all__'
        exclude=['lastlogin', 'userpass','givenname']

class ContractorFilter(django_filters.FilterSet):
    # resource=CharFilter(field_name='givenname',lookup_expr='icontains',label='Name')
    class Meta:
        model = ContractorTracker
        fields= '__all__'
        exclude=['end_date', 'start_date','status','comments']