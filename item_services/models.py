import uuid
from django.db import models

# Create your models here.
class ItemModel(models.Model):
    item_type_choices = [
        ("hats", "hats"),
        ("tops", "tops"),
        ("shorts", "shorts")
    ]
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    item_type = models.CharField(max_length=9, choices=item_type_choices)
    regular_price = models.IntegerField(blank=False)
    vip_price = models.IntegerField(null=True)
    wholesale_price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
