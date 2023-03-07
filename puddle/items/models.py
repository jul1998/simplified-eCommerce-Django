from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
        ordering = ['name']

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Item")
        verbose_name_plural = ("Items")
        ordering = ['name']

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category.serialize(),
        }