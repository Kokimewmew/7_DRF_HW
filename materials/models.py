from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}
class Course(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Название курса', help_text='Укажите курс')

    description = models.TextField(
        **NULLABLE, verbose_name='Описание', help_text='Укажите описание')

    preview_course = models.ImageField(
        upload_to='materials/preview_course', **NULLABLE, verbose_name='Превью', help_text='Укажите превью')

    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Автор")

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Название урока', help_text='Укажите урок')

    course = models.ForeignKey("Course", on_delete=models.SET_NULL, verbose_name='Название курса',
                               help_text='Выберите курс',**NULLABLE, )

    description = models.TextField(
        blank=True, null=True, verbose_name='Описание', help_text='Укажите описание')

    preview_lesson = models.ImageField(
        upload_to='materials/preview_lesson', **NULLABLE, verbose_name='Превью', help_text='Укажите превью')

    link_to_video = models.CharField(max_length=100, **NULLABLE, verbose_name='Ссылка на видео',
                                     help_text='Укажите ссылку')

    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Автор")

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Пользователь")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="Курс")

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
