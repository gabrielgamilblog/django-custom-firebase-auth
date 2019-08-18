from django.db import models

class Tenant(models.Model):
  name = models.CharField(max_length=100)