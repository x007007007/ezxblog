from django.db import models
from django.utils.translation import ugettext as _

from .base import CreateModifyTime


class Media(CreateModifyTime):
    tags = models.ManyToManyField('Tag')
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=32, db_index=True)
    file = models.FileField(upload_to="media/%Y/%m/%d/")

    def __str__(self):
        return "Media<{}:{}>".format(self.type, self.name)