from django import template
from django.db.models.aggregates import Count

from ..models import Post, Category, Tag

register = template.Library()


# 使用这个装饰器就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数
@register.simple_tag
def get_recent_posts(num=5):
	# 返回最近发布的5篇文章
	return Post.objects.all()[:num]


@register.simple_tag
def archives():
	# 返回最近发布文章的5个日期
	return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
	# 记得在顶部引入 count 函数
	# 返回
	return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
	# 记得在顶部引入 Tag model
	return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
