from django.contrib import admin
from basic_app.models import Preorder
# Register your models here.

@admin.register(Preorder)
class PreorderAdmin(admin.ModelAdmin):
    pass
