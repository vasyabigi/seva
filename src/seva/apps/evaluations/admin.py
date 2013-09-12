from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q

from evaluations.models import SelfEvaluation


class SelfEvaluationAdmin(admin.ModelAdmin):
    list_filter = ('level',)
    list_editable = ('level', 'is_favorite')
    list_display = ('user', 'technology', 'level', 'is_favorite')

    def queryset(self, request):
        if not request.user.is_superuser:
            return SelfEvaluation.objects.filter(user=request.user)
        return SelfEvaluation.objects.all()

    def get_form(self, request, obj=None, **kwargs):
        form = super(SelfEvaluationAdmin, self).get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['user'].queryset = User.objects.filter(id=request.user.id)
        return form

admin.site.register(SelfEvaluation, SelfEvaluationAdmin)
