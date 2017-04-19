from django.db import models
from django.utils.translation import ugettext as _

from .base import CreateModifyTime


class KeyValueConfig(CreateModifyTime):
    key = models.CharField(max_length=254, db_index=True, unique=True)
    type = models.CharField(
        max_length=16,
        choices=(
            ('text', 'text'),
            ('json', 'json'),
            ('bool', 'bool'),
            ('int', 'int'),
            ('number', 'number'),
            ('bin', 'bin'),
        )
    )
    text_value = models.TextField(null=True, blank=True)
    bool_value = models.NullBooleanField()
    int_value = models.IntegerField(null=True, blank=True)
    bin_value = models.BinaryField(null=True, blank=True)
    number_value = models.FloatField(null=True, blank=True)