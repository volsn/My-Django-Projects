from django.contrib import admin
from basic_app.models import UserProfileInfo
# Register your models here.

@admin.register(UserProfileInfo)
class UserProfileInfoAdmin(admin.ModelAdmin):
    pass
