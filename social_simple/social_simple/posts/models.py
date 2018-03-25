from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import misaka
from communities.models import Community

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete='SET_NULL')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    community = models.ForeignKey(
        Community,
        related_name='posts',
        null=True,
        blank=True,
        on_delete='SET_NULL')

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={
            'username': self.user.username,
            'pk': self.pk})

    class Meta():
        ordering = ['-created_at']
        unique_together = ['user', 'message']
