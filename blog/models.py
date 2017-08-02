# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published'),
    )

    title = models.CharField('标题',max_length = 40)
    body = models.TextField('正文')
    crete_time = models.DateTimeField('创建时间',auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间',auto_now= True)
    status = models.CharField('文章状态',max_length=1,choices=STATUS_CHOICES)
    abstract = models.CharField('文章摘要',max_length=50,blank=True,help_text="可选，若为空截取正文前50个字符")
    views = models.PositiveIntegerField('浏览量',default=0)
    likes = models.PositiveIntegerField('点赞数',default=0)
    topped = models.BooleanField('置顶',default=False)

    catagory = models.ForeignKey('Category',verbose_name='分类',null=True,on_delete=models.SET_NULL)
    tags = models.ForeignKey('Tag',verbose_name='标签',null=True,on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('blog:article',kwargs={'id':self.id})

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-last_modified_time']

class Category(models.Model):
    names = models.CharField('类名',max_length = 20)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.names

class Tag(models.Model):
    name = models.CharField('标签名',max_length=70)

    def __str(self):
        return self.name
