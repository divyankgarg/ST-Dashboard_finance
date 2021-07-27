from django.contrib import admin
from .models import Accounts, Resources, Functions, LaborAllocations
# Register your models here.
admin.site.register(Accounts)
admin.site.register(Resources)
admin.site.register(Functions)
admin.site.register(LaborAllocations)