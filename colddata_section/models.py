from django.db import models

# Create your models here.
class ColdData(models.Model):
    name_phone = models.CharField(max_length=150, help_text="Name and Phone number combined")
    property_listing = models.TextField(blank=True, null=True, help_text="Details of property listings")

    submitted_at = models.DateTimeField(auto_now_add=True)