from django.db import models
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse

User = get_user_model()
register = template.Library()


class Community(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='Member')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super(Community, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('communities:single', kwargs={'slug': self.slug})

    class Meta():
        ordering = ['name']


class Member(models.Model):
    community = models.ForeignKey(
        Community,
        related_name='memberships',
        on_delete='SET_NULL')
    user = models.ForeignKey(
        User,
        related_name='user_communities',
        on_delete='SET_NULL')

    def __str__(self):
        return self.user.username

    class Meta():
        unique_together = ('community', 'user')
