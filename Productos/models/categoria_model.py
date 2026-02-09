from django.db import models
from django.utils.text import slugify


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre", unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=False, blank=False)

    class Meta:
        db_table = "categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ("-nombre",)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.nombre)
            cont = 1
            prov = base
            while Categoria.objects.filter(slug = prov).exists():
                prov = base + str(cont)
                cont += 1
            self.slug = prov
        super(Categoria, self).save(*args, **kwargs)