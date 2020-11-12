from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage
# Register your models here.

@admin.register(Webpage)
class WebpageAdmin(admin.ModelAdmin):
    pass

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(AccessRecord)
class AccessRecordAdmin(admin.ModelAdmin):
    pass
