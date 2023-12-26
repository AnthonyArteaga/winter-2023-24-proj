from django.contrib import admin
from userauths.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']  #allows us to see these fields easily in admin mode

# Register your models here.
admin.site.register(User, UserAdmin)
