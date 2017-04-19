from django.db import models
from django.conf import locale
from django.utils.translation import ugettext as _

from .base import CreateModifyTime


class Article(CreateModifyTime):
    lang = models.CharField(
        max_length=16,
        choices=zip(locale.LANG_INFO.keys(), locale.LANG_INFO.keys()),
        null=True,
        blank=True
    )
    name = models.CharField(max_length=254)
    tags = models.ManyToManyField('Tag')
    medium = models.ManyToManyField('Media')
    title = models.CharField(max_length=254, null=True, blank=True)
    content_type = models.CharField(
        max_length=16,
        choices=(
            ('html', 'html'),
            ('md', 'md'),
        )
    )
    content = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (('lang', 'name'),)

    def __str__(self):
        return "Article<{}>".format(self.name)
