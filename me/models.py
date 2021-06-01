from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.conf import settings
from django.db import models
import sys
sys.path.append('../')
from wisdom.models import Subject

class Teacher(AbstractUser):
    name = models.CharField(max_length=20, unique=False)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True, blank=True)
    USERNAME_FIELD = 'email'
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True,
    #    on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='teacher_subject',
        null=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['name', 'surname', 'password']

    @receiver(pre_save, dispatch_uid="teacher.username_gen")
    def username_gen(sender, instance, **kwargs):
        if sender != Teacher:
            return
        if not instance.username:
            return
        counter = 0
        username = None
        while True:
            new_username = f'{slugify(instance.surname)}_{slugify(instance.name)}'
            if username:
                username = f'{new_username}_{rand.randint(0,1000)}'
            if not Teacher.objects.filter(username=username).exists():
                break
        instance.username = username
