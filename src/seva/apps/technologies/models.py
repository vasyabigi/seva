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
