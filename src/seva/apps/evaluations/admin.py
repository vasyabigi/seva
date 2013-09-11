from django.contrib import admin

from evaluations.models import SelfEvaluation


class SelfEvaluationAdmin(admin.ModelAdmin):
    list_filter = ('level',)
    list_editable = ('level',)
    list_display = ('user', 'technology', 'level')

admin.site.register(SelfEvaluation, SelfEvaluationAdmin)
