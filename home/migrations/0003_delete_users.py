# Generated by Django 3.2.3 on 2021-05-30 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_users_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
