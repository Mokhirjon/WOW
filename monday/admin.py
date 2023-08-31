from django.contrib import admin
from .models import Week
# Register your models here.
class WeeksAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ['name','id']
admin.site.register(Week,WeeksAdmin)