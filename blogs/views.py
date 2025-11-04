from django.shortcuts import render, get_object_or_404

from blogs.models import Topic, BlogPost
from django.utils.safestring import mark_safe
import markdown
import re


def index(request):
    blogs = BlogPost.objects.order_by('date_added').reverse()
    return render(request, 'blogs/index.html', {'blogs': blogs})


def topics(request):
    topics = Topic.objects.order_by("id")
    context = {"topics": topics}
    return render(request, "blogs/topics.html", context)

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = topic.posts.all().order_by('date_added').reverse()
    return render(request, 'blogs/topic_detail.html', {'topic': topic, 'posts': posts})

def post_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    html = mark_safe(markdown.markdown(
        post.content,
        extensions=[
            'fenced_code',
            'codehilite',  # 这会自动添加 class
            'tables',
        ],
        extension_configs={
            'codehilite': {
                'guess_lang': False,
                'linenums': False,
                'css_class': 'highlight',  # 可以换为 highlight
            }
        }
    ))
    html = re.sub(r'<table>', '<table class="table table-bordered table-striped table-hover">', html)
    rendered_content = mark_safe(html)
    return render(request, 'blogs/post_detail.html', {'post': post, 'rendered_content': rendered_content})
