from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


def check_email_domain(email):
    address, domain = email.split('@')
    if domain == 'rambler.ru':
        raise ValidationError("Регистрация с почтового адреса в домене 'rambler.ru' запрещена")


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLE = [(MEMBER, "Пользователь"), (MODERATOR, "Модератор"), (ADMIN, "Администратор")]

    role = models.CharField(max_length=9, default=MEMBER, choices=ROLE)
    age = models.PositiveIntegerField(null=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, validators=[check_email_domain])
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
