from django.db import models


class Category(models.Model):
    name = models.CharField('Категории', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class TourPayment(models.Model):
    title = models.CharField('Название', max_length=150)
    payment = models.TextField('Способы оплаты')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'


class Tour(models.Model):
    title = models.CharField('Название', max_length=200)
    desc = models.TextField('Описание')
    image = models.ImageField('Главное фото', upload_to='main_photo/')
    places = models.TextField('Планируемые места')
    price = models.PositiveIntegerField('Цена', default=0)
    date = models.DateField("Дата")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(TourPayment, verbose_name="Способ оплаты", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class TourShot(models.Model):
    image = models.ImageField('Изображение', upload_to='shots/')
    tour = models.ForeignKey(Tour, verbose_name='Тур', on_delete=models.CASCADE, related_name="shots")

    class Meta:
        verbose_name = 'Кадр'
        verbose_name_plural = 'Кадры'
