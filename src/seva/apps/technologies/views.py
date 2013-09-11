from django.views.generic import TemplateView
from django.contrib.auth.models import User

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

