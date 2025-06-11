from django.contrib import admin
from .models import formregister
# Register your models here.
@admin.register(formregister)
class AdminUser(admin.ModelAdmin):
    list_display=('id','name','email','password')