import uuid

from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from testproj.utils import slugify, choices
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, verbose_name=_('Created by'), on_delete=models.SET_NULL, editable=False, related_name="created_%(app_label)s_%(class)s_set", null=True, help_text=_('Data created by'))
    modified_by = models.ForeignKey(User, verbose_name=_('Modified by'), on_delete=models.SET_NULL, editable=False, related_name="modified_%(app_label)s_%(class)s_set", null=True, help_text=_('Data modified by'))
    created_on = models.DateTimeField(verbose_name=_('Created on'), auto_now_add=True, help_text=_('Data created on'))
    modified_on = models.DateTimeField(verbose_name=_('Modified by'), auto_now=True, help_text=_('Data modified on'))
    mode = models.CharField(verbose_name=_('Mode'), max_length=30, default='Active', choices=choices.MODE)

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=50, help_text=_('Title'))
    content = RichTextField(verbose_name=_('Content'), help_text=_('Content'))
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title

        slugify.unique_slugify(self, self.slug)
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']


class Comment(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name=_("Article"), related_name="comments")
    text = models.CharField(max_length=200, verbose_name=_("Comment Text"), help_text=_('Title'))

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_on']
