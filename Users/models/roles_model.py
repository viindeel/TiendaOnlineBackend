import secrets

from django.db import models





class Role(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'roles'
        verbose_name = 'Rol de usuario'
        verbose_name_plural = 'Roles de usuarios'
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_hex(8)

            # SELECT * FROM ROle WHERE slug = prov
            while Role.objects.filter(slug=prov).exists():
                prov = secrets.token_hex(8)

            self.slug = prov
            
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}({'activo' if self.is_active else 'inactivo'})"