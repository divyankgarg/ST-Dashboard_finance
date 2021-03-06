# Generated by Django 3.0.6 on 2021-03-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_number', models.IntegerField(blank=True, null=True)),
                ('account', models.CharField(blank=True, max_length=30, null=True)),
                ('labor_type_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'accounts',
                'managed': False,
            },
        ),
    ]
