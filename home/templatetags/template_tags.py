from django import template
from home.models import Social, Post

register = template.Library()

@register.simple_tag
def get_social_links():
    return Social.objects.all().first()

@register.simple_tag
def get_latest_tags():
    posts = Post.objects.all().order_by("-pk")
    tags_list = []
    for post in posts:
        tags = post.tags.split(",")
        for tag in tags:
            if tag not in tags_list: tags_list.append(tag)
            if len(tags_list) == 10: return tags_list
    return tags_list