from django.contrib import admin
from .models import Post
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)


class Post(models.Model):
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"
