from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from datetime import timedelta
from django.utils import timezone


class PaisesChoices(models.TextChoices):
    SPAIN = 'ES', 'ESPAÑA'
    FRANCE = 'FR', 'FRANCIA'
    GERMANY = 'DE', 'ALEMANIA'
    ITALY = 'IT', 'ITALIA'



class InfoPersonal(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="info_personal",
        null=True, blank=True
    )
    document = models.CharField(max_length=15, unique=True, null=True, blank=True, verbose_name='Documento(DNI, NIE, Pasaporte)', help_text='Obligatorio')
    phone = models.CharField(max_length=11, unique=True, verbose_name='Telefono', help_text='Opcional', null=True, blank=True )
    age = models.PositiveIntegerField(
        null=False, blank=False, default=18, choices=[(n, n) for n in range(1, 101)], verbose_name='Edad'
                                      )
    birthday = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento', help_text='Obligatorio')
    # LEGAL_BASE_AGE = 13
    address = models.TextField(null=True, blank=True, verbose_name='Direccion', help_text='Obligatorio')

    city = models.ForeignKey("CiudadModel", on_delete=models.SET_NULL, max_length=50, null=True, blank=True, verbose_name='Ciudad', help_text='Obligatorio')

    country = models.CharField(max_length=3, choices=PaisesChoices.choices, default=PaisesChoices.SPAIN ,
                                verbose_name='Pais', help_text='Obligatorio')

    

    class Meta:
        db_table = 'info_personal'
        verbose_name = 'Informacion Personal'
        verbose_name_plural = 'Datos Personales'
        ordering = ('-country',)

    def __str__(self):
        return f'{self.document} - {self.country} - {self.city}'
    #
    # def clean(self):
    #     super().clean()
    #     # if self.phone:
    #     #     if len(self.phone) != 9:
    #     #         raise ValidationError('El telefono debe ser un numero de 9 digitos')
    #     # if self.birthday:
    #     #     if self.birthday > timezone.now().date() - timedelta(days=365.25 * self.LEGAL_BASE_AGE):
    #     #         raise ValidationError('Debes tener al menos 13 años para registrarte')
    #
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    # def delete(self, *args, **kwargs):
    #     self.is_active = False
    #     self.save()