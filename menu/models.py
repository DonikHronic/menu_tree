from django.db import models
from django.urls import reverse


class Content(models.Model):
	text = models.ManyToManyField('PageContent')

	class Meta:
		db_table = 'content'
		verbose_name = 'Контент'
		verbose_name_plural = 'Контент'


class PageContent(models.Model):
	page_content = models.TextField('Тексты')

	class Meta:
		db_table = 'page_content'
		verbose_name = 'Содержание страницы'
		verbose_name_plural = 'Содержание страниц'


class StaticPages(models.Model):
	"""Страницы меню"""
	name = models.CharField('Название страницы', max_length=50)
	slug = models.SlugField('Ссылка на страницу', unique=True)
	menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
	content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True, blank=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_menu')
	is_child = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if not self.content:
			content = Content.objects.create()
			self.content = content
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	@property
	def get_parent(self):
		if not self.parent:
			return ''
		return self.parent.id

	def get_absolute_url(self):
		return reverse('flatpage', kwargs={'slug': self.slug})

	class Meta:
		db_table = 'static_pages'
		verbose_name = 'Страница'
		verbose_name_plural = 'Страницы'


class Menu(models.Model):
	"""Названия меню"""
	name = models.CharField('Название', max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'menu'
		verbose_name = 'Меню'
		verbose_name_plural = 'Меню'
