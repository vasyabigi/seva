from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User)
    joined = models.DateField(blank=True, null=True)
    number = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dont_track_in_avg = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

    def is_active():
        return self.user.is_active

    def get_avg_level(self):
        return self.user.selfevaluation_set.\
            aggregate(models.Avg('level'))['level__avg']


@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    """
    Creates profile for user if it's not exist.
    """
    try:
        profile = instance.profile
    except Profile.DoesNotExist:
      p = Profile(user=instance)
      p.save()
