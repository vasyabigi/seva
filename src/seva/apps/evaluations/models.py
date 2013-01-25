from django.db import models
from django.contrib.auth.models import User

from technologies.models import Technology


class Evaluation(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    technology = models.ForeignKey(Technology)
    level = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s %s" % (self.user, self.technology)


class SelfEvaluation(Evaluation):
    is_favorite = models.BooleanField()


