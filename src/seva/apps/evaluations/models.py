from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from technologies.models import Technology


def validate_level(value):
    if value not in xrange(11):
        raise ValidationError(u'Level value must be between 1 and 10')


class Evaluation(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    technology = models.ForeignKey(Technology)
    level = models.PositiveIntegerField(default=0,
        validators=[validate_level,]
    )

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s %s" % (self.user, self.technology)


class SelfEvaluation(Evaluation):
    is_favorite = models.BooleanField()


