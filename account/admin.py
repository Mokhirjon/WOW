from django.contrib import admin
from  django.contrib.auth.admin import UserAdmin
from .models import Customuser
from .forms import CustomusersCReate,CustomusersUpdate
# Register your models here.
class CustomuserAdmin(UserAdmin):
    add_form = CustomusersCReate
    form = CustomusersUpdate
    model = Customuser
    list_display = ['username','password','role','phone']
    fieldsets = (
        (None,{
            "fields":(
                'username', 'password',
                'role', 'phone'
            ),
        }),
    )
admin.site.register(Customuser,CustomuserAdmin)