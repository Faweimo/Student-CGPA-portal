from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Department,User,College,Profile

# Register your models here.
class UserAdmin(UserAdmin):
    list_display =('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    search_fields = ('first_name',)
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(User,UserAdmin)
admin.site.register(Department)
admin.site.register(College)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','department',)
    # list_filter = ('matric_no',)

admin.site.register(Profile,ProfileAdmin)