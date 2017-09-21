# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 21:32
# @Author  : yj

from ..models import Post,Category,Tag

from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    '''
    最新文章标签
    :param num: 
    :return: 
    '''
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_hot_article(num=5):
    '''
    点击量最高的文章
    :param num:
    :return:
    '''
    return Post.objects.all().order_by('-views')[:num]


@register.simple_tag
def archives():
    '''
    归档模板标签,dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，且是 Python 的 date 对象，精确到月份，降序排列
    :return: 
    '''
    return Post.objects.dates('created_time','month',order='DESC')


@register.simple_tag
def get_categories():
    '''
    分类模板标签
    :return: 
    '''
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post'))


@register.simple_tag
def get_tags():
    '''
    云标签
    :param num: 
    :return: 
    获取到文章数大于 0 的标签列表
    '''
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

