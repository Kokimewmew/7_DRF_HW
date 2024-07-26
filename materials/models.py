from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Название курса', help_text='Укажите курс')

    description = models.TextField(
        blank=True, null=True, verbose_name='Описание', help_text='Укажите описание')

    preview_course = models.ImageField(
        upload_to='materials/preview_course', blank=True, null=True, verbose_name='Превью', help_text='Укажите превью')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Название урока', help_text='Укажите урок')

    course = models.ForeignKey("Course", on_delete=models.SET_NULL, verbose_name='Название курса',
                               help_text='Выберите курс', null=True, blank=True, )

    description = models.TextField(
        blank=True, null=True, verbose_name='Описание', help_text='Укажите описание')

    preview_lesson = models.ImageField(
        upload_to='materials/preview_lesson', blank=True, null=True, verbose_name='Превью', help_text='Укажите превью')

    link_to_video = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на видео',
                                     help_text='Укажите ссылку')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
