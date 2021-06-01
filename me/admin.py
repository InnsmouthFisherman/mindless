from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from me.models import Teacher


class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    verbose_name_plural = 'teachers'
    list_display = ['name', 'surname', 'subject']

class UserTeacher(BaseUserAdmin):
    inlines = (TeacherInline,)

admin.site.register(User, UserTeacher)
admin.site.register(Teacher)
