# Generated by Django 2.2.4 on 2021-05-11 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wisdom', '0001_initial'),
        ('me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='wisdom.Subject'),
            preserve_default=False,
        ),
    ]
