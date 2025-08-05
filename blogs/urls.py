from django_distill import distill_path
from . import views
from .models import Topic, BlogPost

app_name = "blogs"

def get_none():
    return [None]

def get_topic_ids():
    return [(topic.id,) for topic in Topic.objects.all()]

def get_post_ids():
    return [(post.pk,) for post in BlogPost.objects.all()]

urlpatterns = [
    distill_path("", views.index, name="index", distill_func=get_none),

    distill_path("topics/", views.topics, name="topics", distill_func=get_none),

    distill_path("topics/<int:topic_id>/", views.topic_detail, name="topic_detail", distill_func=get_topic_ids),

    distill_path("post/<int:pk>/", views.post_detail, name="post_detail", distill_func=get_post_ids),
]