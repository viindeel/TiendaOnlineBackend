import secrets

from django.db import models


class Productos(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre", unique=True, null=False, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio", null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripcion", null=True, blank=True)
    categoria = models.ForeignKey("Categoria", on_delete=models.PROTECT, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=False, blank=False)

    class Meta:
        db_table = "productos"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ("-nombre",)

    def __str__(self):
        return f"{self.nombre} - {self.categoria.nombre}"


    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_hex(8)
            while Productos.objects.filter(slug = prov).exists():
                prov = secrets.token_hex(8)
            self.slug = prov
        super(Productos, self).save(*args, **kwargs)
