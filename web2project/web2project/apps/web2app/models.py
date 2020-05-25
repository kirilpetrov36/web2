from django.db import models
from django.utils import timezone

class User(models.Model):
	username = models.CharField('Никнейм', max_length=20)
	password = models.CharField('Пароль', max_length=20)
	note_amount = models.IntegerField('Кол-во заметок', default=0)
	last_online = models.DateTimeField('Последний раз в сети', default=timezone.now())
	admin = models.BooleanField('Админка', default=False)

	def __str__(self):
		return self.username

class Note(models.Model):
	theme = models.CharField('Тема заметки', max_length = 30)
	text = models.TextField('Текст заметки', max_length = 404)
	date = models.DateTimeField('Дата создания')
	last_edit = models.DateTimeField('Дата ласт изменения')
	last_user = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.theme