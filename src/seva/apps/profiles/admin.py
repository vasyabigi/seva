from django.contrib import admin

from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'joined', 'number' )
    list_editable = ('joined', 'number')

admin.site.register(Profile, ProfileAdmin)
