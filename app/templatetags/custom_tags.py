from django import template
from django.template.loader_tags import do_include
from django.template.base import TemplateSyntaxError, Token


register = template.Library()


@register.tag('xinclude')
def xinclude(parser, token):
    '''
    {% xinclude "blogs/blog{}.html/" "123" %}
    '''
    bits = token.split_contents()
    if len(bits) < 3:
        raise TemplateSyntaxError(
            "%r tag takes at least two argument: the name of the template to "
            "be included, and the variable" % bits[0]
        )
    template = bits[1].format(bits[2])
    # replace with new template
    bits[1] = template
    # remove variable
    bits.pop(2)
    new_content = ' '.join(bits)
    new_token = Token(token.token_type, new_content)
    return do_include(parser, new_token)
