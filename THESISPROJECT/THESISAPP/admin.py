from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class registeradmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('first_name','last_name','username','email','password1','password2','is_admin','is_client'),
        }),
    )
admin.site.register(User, registeradmin)
admin.site.register(Product)
admin.site.register(LotOrder)