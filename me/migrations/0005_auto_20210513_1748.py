# Generated by Django 2.2.4 on 2021-05-13 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0004_teacher_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_subject', to='wisdom.Subject'),
        ),
    ]