from django.db import models
from django.utils.translation import ugettext as _


class CreateModifyTime(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_time = models.DateTimeField(auto_now=True, null=True, blank=True)