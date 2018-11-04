from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=80)
    banner = models.ImageField(upload_to='apps/banners', default=None)
    description = models.CharField(max_length=80)