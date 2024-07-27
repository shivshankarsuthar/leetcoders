from django.contrib import admin
from accounts.models import *
from django.contrib.admin import AdminSite
# Register your models here.
class AdminSite(AdminSite):
    site_header = 'Account'
    site_title = 'Account Admin'
    site_url = '/api/account'

admin_site = AdminSite(name='account_admin')
admin.register(admin_site)