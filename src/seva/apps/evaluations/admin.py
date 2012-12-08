from django.contrib import admin

from evaluations.models import SelfEvaluation


class SelfEvaluationAdmin(admin.ModelAdmin):
    pass

admin.site.register(SelfEvaluation, SelfEvaluationAdmin)
