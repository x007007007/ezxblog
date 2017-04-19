from django.db import models
from django.utils.translation import ugettext as _

from .base import CreateModifyTime


class Tag(CreateModifyTime):
    name = models.CharField(max_length=254, db_index=True)

    def __str__(self):
        return "Tag<{}>".format(self.name)