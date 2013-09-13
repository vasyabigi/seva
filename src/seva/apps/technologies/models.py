from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to='tech/logos',
        blank=True, null=True
    )
    category = models.ForeignKey(Category, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class TechnologyLevelDescription(models.Model):
    technology = models.ForeignKey(Technology)
    level = models.PositiveIntegerField()
    description = models.TextField()

    def __unicode__(self):
        return self.level


class KeyMetrics(models.Model):
    technology = models.ForeignKey(Technology)
    metric_description = models.TextField()

    def __unicode__(self):
        return self.technology.title


@receiver(post_save, sender=Technology)
def create_profile_for_user(sender, instance, created, **kwargs):
    """
    Creates selfevaluations
    """
    from evaluations.models import SelfEvaluation
    for user in User.objects.all():
        evl, created = SelfEvaluation.objects.get_or_create(technology=instance, user=user)