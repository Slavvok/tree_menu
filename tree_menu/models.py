from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    parent = models.ForeignKey("self", related_name='children', null=True, blank=True, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name
