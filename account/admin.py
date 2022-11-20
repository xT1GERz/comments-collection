from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Register your models here.
class AdminManager(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('username', 'email')  # these fields in users list,
    # will open that account's page when clicked
    readonly_fields = ('date_joined', 'last_login')  # these fields can not change at all
    ordering = ('-date_joined', )  # sort users list by date_joined descending order
    filter_horizontal = ()
    list_filter = ()

admin.site.register(Account, AdminManager)