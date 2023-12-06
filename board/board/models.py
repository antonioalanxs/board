import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        to_field="username",
        db_column="author",
        on_delete=models.CASCADE,
    )
    slug = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
