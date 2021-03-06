from django.db import models
from django.urls import reverse

# Create your models here.
class Hashtag(models.Model):
    content = models.TextField(unique=True)
    detect = models.CharField(max_length=500, default="alert alert-light")
    def __str__(self):
        return self.content

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"article_pk": self.pk})

class Comment(models.Model):
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.content


    


