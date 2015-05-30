#!/usr/bin/env python
# encoding: utf-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

from django.contrib.admin import ModelAdmin, site
from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
STATUS_CHOICES = (
    ('0', u"草稿"),
    ('1', u"发布"),
    ('2', u"私密"),
)

class Gallery(models.Model):
    title = models.CharField(_('Title'), max_length=250)
    description = models.TextField(_('Description'))
    user = models.ForeignKey(User, null=True, blank=True, editable=False)
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(_('Update Time'), auto_now=True)
    status = models.CharField(_('Status'), max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    class Meta:
        ordering = ['title']
        verbose_name_plural = _('Gallery')
        
    def __str__(self):
        return self.title
        

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, null=True, blank=True)
    title = models.CharField(_('Title'), max_length=100,null=True, blank=True)
    #file = ThumbnailImageField(_('File'), upload_to='photos')
    caption = models.CharField(_('Caption'), max_length=250, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, editable=False)
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(_('Update Time'), auto_now=True)
    status = models.CharField(_('Status'), max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = _('Image')        

