from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_description = models.CharField(max_length=200)
    item_image = models.CharField(max_length=500,
                                  default="https://placehold.co/600x400.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
