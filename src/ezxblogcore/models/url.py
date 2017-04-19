from django.db import models
from django.utils.translation import ugettext as _

from .base import CreateModifyTime


class Url(CreateModifyTime):
    path = models.CharField(max_length=254, db_index=True, unique=True)
    type = models.CharField(
        max_length=32,
        choices=(
            ('article', 'article'),
        )
    )
    full_url = models.TextField(max_length=2046, null=True, blank=True)

    def __str__(self):
        return "url<{}>".format(self.path)