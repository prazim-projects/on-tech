from django.db import models
from django.utils import timezone
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    flag = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
class flag(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='post_flag')
    flag_1 = models.CharField(max_length=255)

    def __str__(self):
        return f'Flag for {self.post.title}'
