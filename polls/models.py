from django.db import models
from django.urls import reverse


class Polls(models.Model):
    """Голосования"""
    title = models.CharField('Голосование', max_length=200)
    name = models.CharField('Название голосования', max_length=200)
    start = models.DateTimeField('Дата начала')
    finish = models.DateTimeField('Дата завершения')
    max_count_votes = models.PositiveIntegerField(
        'Максимальное число голосов для победы', default=0)
    active = models.BooleanField('Статус')
    url = models.SlugField(max_length=160, unique=True, default='url')

    def get_absolute_url(self):
        return reverse('polls:detail', kwargs={'slug': self.url})

    def get_absolute_result_url(self):
        return reverse('polls:result', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'

    def __str__(self):
        return self.title


class Persons(models.Model):
    """Кандидаты"""
    img = models.ImageField('Фотография', upload_to='persons/')
    name = models.CharField('Имя', max_length=200)
    middle_name = models.CharField('Отчество', max_length=200)
    surname = models.CharField('Фамилия', max_length=200)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    bio = models.TextField('Краткая биография')
    votes = models.PositiveIntegerField("Голоса", default=0)
    polls = models.ForeignKey(Polls, verbose_name='Голосования',
                              on_delete=models.CASCADE, default=0)

    class Meta:
        verbose_name = 'Кандитат'
        verbose_name_plural = 'Кандидаты'
        ordering = ["-votes"]

    def __str__(self):
        return self.name
