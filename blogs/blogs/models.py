from django.db import models
from django.contrib.auth.models import User
from .settings import STATIC_URL

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    preview_image = models.ImageField(upload_to=f'{STATIC_URL}post_images/', null=True, blank=True)
    detail_image = models.ImageField(upload_to=f'{STATIC_URL}post_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

class GalleryImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to=f'{STATIC_URL}post_gallery/')

    def __str__(self):
        return f"Image for {self.post.title}"
