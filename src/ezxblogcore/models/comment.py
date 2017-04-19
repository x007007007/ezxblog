from django.db import models
from django.utils.translation import ugettext as _

from .base import CreateModifyTime


class Comment(models.Model):
    type = models.CharField(
        max_length=32,
        choices=(
            ('article', 'article'),
            ('comment', 'comment')
        )
    )
    on_article = models.ForeignKey("Article")
    on_comment = models.ForeignKey('Comment', null=True, blank=True)

    message = models.TextField(max_length=1024)

    def __str__(self):
        return "Comment<{}:{}>".format(self.on_article.name, self.pk)