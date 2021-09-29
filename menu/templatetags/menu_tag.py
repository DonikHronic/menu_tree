from django import template

from menu.models import StaticPages, Menu
from menu.utils import create_menu_tree

register = template.Library()


@register.simple_tag()
def draw_menu(name):
	menu = Menu.objects.get(name=name)
	pages = StaticPages.objects.filter(menu=menu.id, parent=None)
	if pages:
		tree = create_menu_tree(pages)
	else:
		tree = ''
	return tree
