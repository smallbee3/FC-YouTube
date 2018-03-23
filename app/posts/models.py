from django.conf import settings
from django.db import models
from django.utils import timezone


def dynamic_profile_img_path(instance, filename):
    return f'video/{instance.category}/{filename}'


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=300, blank=True)
    img_thumbnail = models.ImageField(
        upload_to=dynamic_profile_img_path,
        blank=True,
        null=True,
    )

    category = models.CharField(max_length=100)
    youtube_link = models.CharField(max_length=1000)
    script = models.TextField(max_length=50000, blank=True)

    created_date = models.DateTimeField(default=timezone.now)
    recorded_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author.username})'

    class Meta:
        ordering = ['-pk']


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment (PK: {self.pk}, Author: {self.author.username})'


