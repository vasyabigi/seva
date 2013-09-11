from django.contrib import admin

from technologies.models import (Category, Technology,
    TechnologyLevelDescription, KeyMetrics)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'slug')



class KeyMetricsInline(admin.TabularInline):
    model = KeyMetrics

class TechnologyLevelDescriptionInline(admin.TabularInline):
    model = TechnologyLevelDescription


class TechnologyAdmin(admin.ModelAdmin):
    inlines = [TechnologyLevelDescriptionInline, KeyMetricsInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Technology, TechnologyAdmin)
