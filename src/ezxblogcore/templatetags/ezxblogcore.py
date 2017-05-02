from __future__ import absolute_import, unicode_literals
from django import template
register = template.Library()
from ..models import Article


@register.tag(name="list_article")
def do_list_article(parser, token):
    print(parser, token)
    nodelist = parser.parse(('end_list_article',))
    parser.delete_first_token()
    return ListArticleNode(nodelist, token)


class ListArticleNode(template.Node):
    def __init__(self, nodelist, token):
        self.nodelist = nodelist
        self.token = token


    def render(self, context):
        outputs = []
        for article in Article.objects.filter():
            output = self.nodelist.render(context)
            outputs.append(output)

        return "".join(outputs)