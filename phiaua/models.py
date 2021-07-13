from django.db import models


class Khuán(models.Model):
    miâ = models.CharField(max_length=30, unique=True)
    iūnn = models.CharField(max_length=30)

    def __str__(self):
        return self.miâ

    class Meta:
        verbose_name = "Khuán"
        verbose_name_plural = verbose_name


class Luī(models.Model):
    khuán = models.ForeignKey(
        Khuán,
        related_name='luī',
        on_delete=models.PROTECT,
    )
    miâ = models.CharField(max_length=30, unique=True)
    siktsuí = models.CharField(max_length=10)
    singāu = models.PositiveIntegerField()

    def __str__(self):
        return self.miâ

    class Meta:
        verbose_name = "Luī"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['khuán', 'miâ'],
                name='khuán-luī',
            ),
        ]
