# Generated by Django 2.2.4 on 2021-05-12 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wisdom', '0001_initial'),
        ('me', '0003_remove_teacher_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='teacher_subject', to='wisdom.Subject'),
            preserve_default=False,
        ),
    ]
