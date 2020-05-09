# Python imports
import uuid

# Django imports
from django.db import models


class Share(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    uid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False
    )
    is_locked = models.BooleanField(default=False)
    is_edit_allowed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name if self.name else F"Share {self.uid}"
