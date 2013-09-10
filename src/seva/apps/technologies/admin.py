from django.contrib import admin

from technologies.models import Category, Technology


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'slug')


class TechnologyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Technology, TechnologyAdmin)
