def build_tree_branches(json_obj, parent_id):
	menu_list = '<ul class="hide child__list">'
	for obj in json_obj:
		if obj["parent"] == parent_id:
			menu_list += f'''
				<li class="child__list-item">
					<a href="/{obj['slug']}/">{obj['name']}</a>
			'''

			if build_tree_branches(json_obj, obj["id"]):
				menu_list += build_tree_branches(json_obj, obj["id"])
			menu_list += '</li>'

	menu_list += '</ul></li>'
	return menu_list


def build_tree(json_obj):
	menu_list = '<ul class="main__list">'

	for obj in json_obj:
		if not obj["parent"]:
			menu_list += f'''
				<li class="main__list-item">
					<a href="/{obj['slug']}/">{obj['name']}</a>
			'''

			if build_tree_branches(json_obj, obj["id"]):
				menu_list += build_tree_branches(json_obj, obj["id"])
			menu_list += '</li>'

	menu_list += '</ul>'
	return menu_list
