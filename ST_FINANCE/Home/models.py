from django.db import models
from django.apps import AppConfig
from multiselectfield import MultiSelectField
from datetime import date, datetime
from django.utils import timezone
from django.db.models.query import QuerySet

# Create your models here.
class Functions(models.Model):
    function = models.AutoField(primary_key=True) #function_id to function
    function_name = models.CharField(max_length=20, blank=True, null=True) #function to function_name

    class Meta:
        managed = True
        db_table = 'functions'
    def __str__(self):
        return self.function_name #put self.function_name too it will be same and remove return it will be same

class Geography(models.Model):
    geo = models.AutoField(primary_key=True) #geo_id to geo changed
    geography = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=20)
    labor_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geography'
    def __str__(self):
        return self.geography #put self.function_name too it will be same and remove return it will be same


class Resources(models.Model):
    Test_category=(
        (0,0),(1,1),
        )
    resource_num = models.AutoField(primary_key=True)
    resource = models.CharField(max_length=80)
    geo = models.ForeignKey(Geography, on_delete=models.CASCADE, null=True)
    function = models.ForeignKey(Functions, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(choices=Test_category)

    class Meta:
        managed = True
        db_table = 'resources'
    def __str__(self):
        return self.resource

class ProjectTypes(models.Model):
    project_type = models.AutoField(primary_key=True)
    project_type_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_types'
    def __str__(self):
        return self.project_type_name

class BuList(models.Model):
    bu_num = models.AutoField(primary_key=True)
    bu = models.CharField(max_length=20, blank=True, null=True)
    bg_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bu_list'
    def __str__(self):
        return self.bu

class Projects(models.Model):
    Test_category=(
        (0,0),(1,1),
        )
    project_num = models.AutoField(primary_key=True)
    project = models.CharField(unique=True, max_length=64, blank=True, null=True)
    project_type = models.ForeignKey(ProjectTypes,on_delete=models.CASCADE)
    bu_num = models.ForeignKey(BuList,on_delete=models.CASCADE)
    project_description = models.CharField(max_length=300, blank=True, null=True)
    active = models.BooleanField(choices=Test_category)

    class Meta:
        managed = False
        db_table = 'projects'
    def __str__(self):
        return self.project


class Programs(models.Model):
    program_num = models.AutoField(primary_key=True)
    program = models.CharField(unique=True, max_length=64, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'programs'
    def __str__(self):
        return self.program
        
class LaborAllocations(models.Model):
    function_id = models.IntegerField(blank=True, null=True)
    project_num = models.ForeignKey(Projects, on_delete=models.CASCADE) #,related_name='project_rel'
    resource_num = models.ForeignKey(Resources, on_delete=models.CASCADE,verbose_name='Resource Name') #,related_name='resource_rel'
    component_id = models.IntegerField()
    activity = models.CharField(max_length=80, blank=True, null=True)
    quarter = models.CharField(max_length=4, blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated')  # Field name made lowercase.
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'labor_allocations'
        # unique_together = (( 'project_id', 'resource_num', 'component_id', 'activity', 'quarter'),)
    def __str__(self):
        return self.activity


class Accounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_number = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=30, blank=True, null=True)
    labor_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'

    def __str__(self):
        return self.account

class Users(models.Model):
    Test_category=(
        ('read','read'),('write','write'),('admin','admin')
        )
    userid = models.CharField(db_column='userId', unique=True, max_length=50)  # Field name made lowercase.
    userpass = models.CharField(max_length=32, blank=True, null=True)
    givenname = models.CharField(db_column='givenName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(max_length=20,choices=Test_category, blank=True, null=True)
    bu = models.CharField(max_length=12, blank=True, null=True)
    lastlogin = models.DateTimeField(db_column='lastLogin',default= timezone.now)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('id', 'userid'),)

class ContractorTracker(models.Model):
    name = models.CharField(max_length=64)
    vendor = models.CharField(max_length=64)
    geo = models.ForeignKey(Geography, on_delete=models.CASCADE, null=True)#models.IntegerField(blank=True, null=True) 
    manager = models.CharField(max_length=32, blank=True, null=True)
    function = models.ForeignKey(Functions, on_delete=models.CASCADE, null=True)#models.IntegerField(blank=True, null=True) 
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    rate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    qtr_rate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    comments = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contractor_tracker'

    def __str__(self):
        return self.name
