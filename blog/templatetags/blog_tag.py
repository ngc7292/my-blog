from ..models import Article
from django import template

register = template.Library()

@register.simple_tag
def get_recent_tag(num = 5):
    return Article.objects.all().order_by('crete_time')[:num]