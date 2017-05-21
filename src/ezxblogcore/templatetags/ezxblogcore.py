from __future__ import absolute_import, unicode_literals
from django import template
register = template.Library()
from ..models import Article


@register.tag(name="list_article")
def do_list_article(parser, token):
    """

    {% list_article %}
    {% list_article as article : lang in [], tags in [], filter_{}=aaa, filter_{}=bbb %}
    :param parser:
    :param token:
    :return:
    """
    print(token.split_contents())
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
            context["article"] = article
            output = self.nodelist.render(context)
            outputs.append(output)

        return "".join(outputs)