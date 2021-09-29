from django.contrib import admin

from menu.models import StaticPages, Menu


@admin.register(StaticPages)
class StaticPagesAdmin(admin.ModelAdmin):
	pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	pass
