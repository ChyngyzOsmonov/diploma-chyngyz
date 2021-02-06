from django.db import models


class Tour(models.Model):
    title = models.CharField('Название', max_length=200)
    desc = models.TextField('Описание')
    image = models.ImageField('Главное фото', upload_to='main_photo/')
    image2 = models.ImageField('Изображение-2', upload_to='shots/')
    image3 = models.ImageField('Изображение-3', upload_to='shots/')
    image4 = models.ImageField('Изображение-4', upload_to='shots/')
    places = models.TextField('Планируемые места')
    payment = models.TextField('Способы оплаты')
    price = models.PositiveIntegerField('Цена', default=0)
    date = models.DateField("Дата")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

