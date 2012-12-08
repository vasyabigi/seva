from django.contrib import admin

from technologies.models import Category, Technology


class CategoryAdmin(admin.ModelAdmin):
    pass


class TechnologyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Technology, TechnologyAdmin)
