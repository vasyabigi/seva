from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User)
    joined = models.DateTimeField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username

    def is_active():
        return self.user.is_active

    def get_avg_level(self):
        return self.user.selfevaluation_set.\
            aggregate(models.Avg('level'))['level__avg']
