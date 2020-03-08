from django import template

from ..models import *

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, slug):
    parentmenu = Menu.objects.filter(slug=slug, is_main=True)
    if not parentmenu.exists():
        raise Exception(f"No such main menu: {slug}")
    return {'menus': parentmenu, 'request': context['request']}


@register.filter
def current_path(path, slug):
    return True if slug == path.split('/')[-2] else False
