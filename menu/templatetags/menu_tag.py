import json

from django import template

from menu.api.serializers import StaticPagesSerializer
from menu.models import StaticPages, Menu
from menu.utils import build_tree

register = template.Library()


@register.simple_tag()
def draw_menu(name):
	menu = Menu.objects.get(name=name)
	pages = StaticPages.objects.filter(menu=menu.id)

	serializer = StaticPagesSerializer(pages, many=True)
	menu_json = json.loads(json.dumps(serializer.data, ensure_ascii=False))

	if pages:
		return build_tree(menu_json)
	return ''
