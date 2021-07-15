from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок новости")
    text = models.TextField(verbose_name="Текст новости")
    date = models.DateField(auto_now_add=True, verbose_name="Дата новости")

    def __str__(self):
        return self.title
