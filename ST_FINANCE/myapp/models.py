# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

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