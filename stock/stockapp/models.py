from django.db import models
from django.utils import timezone


class Stock(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    stock_value = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        null=True, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
