from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.text


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    topic = models.ManyToManyField(Topic, related_name='posts')
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title