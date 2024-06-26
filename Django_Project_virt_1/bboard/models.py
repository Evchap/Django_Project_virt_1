from django.db import models

class Bb(models.Model): # 50
	title = models.CharField(max_length=50, verbose_name='Товар')
	content = models.TextField(null=True, blank=True, verbose_name='Описание') #
	price = models.FloatField(null=True, blank=True, verbose_name='Цена')
	published = models.DateTimeField(auto_now_add=True,  null=True, db_index=True, verbose_name='Опубликовано')
	rubric = models.ForeignKey('Rubric', null = True, on_delete=models.PROTECT, verbose_name ='Рубрика') # 54

	class Meta:
		verbose_name_plural = 'Объявления'
		verbose_name = 'Объявление'
		ordering = ['-published']


class Rubric(models.Model): # стр 53
	name = models.CharField(max_length=20, db_index=True, verbose_name='Название')


	def __str__(self): # отображение в строковом виде стр 55
		return self.name

	class Meta:
		verbose_name_plural = 'Рубрики'
		verbose_name = 'Рубрика'
		ordering = ['name']
