from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.ForeignKey(User)
    joined = models.DateTimeField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username

    def is_active():
        return self.user.is_active
