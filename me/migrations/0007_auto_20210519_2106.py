# Generated by Django 2.2.4 on 2021-05-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0006_auto_20210513_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
