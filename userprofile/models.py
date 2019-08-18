from django.db import models
from django.contrib.auth.models import User

from tenant.models import Tenant


class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete='CASCADE')
  tenant = models.ForeignKey(Tenant, on_delete='CASCADE')