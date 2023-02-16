from django.db import models
from django.utils import timezone
# Create your models here.

class Categories(models.Model):
    name  = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Categories")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Todolist(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now().strftime("%d-%m-%Y"))
    due_date = models.DateTimeField(default=timezone.now().strftime("%d-%m-%Y"))
    category = models.ForeignKey(Categories, default='Random Task', on_delete=models.CASCADE)

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return self.title