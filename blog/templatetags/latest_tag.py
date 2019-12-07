from django import template
from blog.models import Post


register = template.Library()



@register.simple_tag
def latest_post():
    postal = Post.objects.filter(tags__name__contains='Travel')
    context = {'postal': postal}
    return context


@register.simple_tag
def total_count():
    post = Post.objects.all()
    return post.count()









