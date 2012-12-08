from django.contrib import admin

from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', )

admin.site.register(Profile, ProfileAdmin)
