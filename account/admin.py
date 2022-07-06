from django.contrib import admin
from .models import Profile
from appraisal_component.models import User

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'dob', 'photo', 'level', 'gender', 'department', 'bio', 'staff_id', ]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'first_name', 'last_name', 'email', 'account_type']
