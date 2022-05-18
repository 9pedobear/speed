from django.db import models

class Product(models.Model):
    file = models.FileField(
        upload_to='images/%Y/%m/%d',
        blank=True
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    description = models.TextField(
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    is_published = models.BooleanField(
        default=True
    )
    price = models.IntegerField(
        default=0,
        blank=True
    )

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    email = models.EmailField(
        blank=True,
    )
    phone = models.CharField(
        max_length=10,
        blank=True
    )
    massage = models.TextField(
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.name}'


