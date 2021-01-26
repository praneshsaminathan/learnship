# import uuid
# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth import get_user_model
# from testproj.utils import choices
# User = get_user_model()
#
#
# class BaseModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     created_by = models.ForeignKey('User', verbose_name=_('Created by'), on_delete=models.SET_NULL, editable=False, related_name="created_%(app_label)s_%(class)s_set", null=True, help_text=_('Data created by'))
#     modified_by = models.ForeignKey('User', verbose_name=_('Modified by'), on_delete=models.SET_NULL, editable=False, related_name="modified_%(app_label)s_%(class)s_set", null=True, help_text=_('Data modified by'))
#     created_on = models.DateTimeField(verbose_name=_('Created on'), auto_now_add=True, help_text=_('Data created on'))
#     modified_on = models.DateTimeField(verbose_name=_('Modified by'), auto_now=True, help_text=_('Data modified on'))
#     mode = models.CharField(verbose_name=_('Mode'), max_length=30, default='Active', choices=choices.MODE)
#
#     class Meta:
#         abstract = True
#
