def get_children(queryset_child):
	menu_list = '<ul class="hide child__list">'

	for page_menu in queryset_child:
		menu_list += f'''
			<li class="child__list-item">
				<a href="{page_menu.get_absolute_url()}">{page_menu.name}</a>
		'''

		if page_menu.child_menu.exists():
			menu_list += get_children(page_menu.child_menu.all())

	menu_list += '</li></ul></li>'
	return menu_list


def create_menu_tree(queryset):
	menu_list = '<ul class="main__list">'

	for page_menu in queryset:
		menu_list += f'''
		<li class="main__list-item">
			<a href="{page_menu.get_absolute_url()}">{page_menu.name}</a>
		'''

		if page_menu.child_menu.exists():
			menu_list += get_children(page_menu.child_menu.all())
		if not page_menu.is_child:
			menu_list += '</li>'

	menu_list += '</ul>'
	return menu_list
