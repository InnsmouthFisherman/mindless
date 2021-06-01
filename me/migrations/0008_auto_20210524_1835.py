# Generated by Django 2.2.4 on 2021-05-24 13:35
from django.db.models import Q
from django.db import migrations, models

def forwards_func(apps, schema_editor):
    Teachers = apps.get_model("me", "Teacher")
    db_alias = schema_editor.connection.alias
    for x in Teachers.objects.filter(models.Q(email='')|models.Q(email__isnull='')):
        x.email = f'fake_email_{x.pk}@fake_email.fake'
        x.save()

class Migration(migrations.Migration):

    dependencies = [
        ('me', '0007_auto_20210519_2106'),
    ]

    operations = [
        migrations.RunPython(forwards_func), # <= Порядок имеет значение

        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
