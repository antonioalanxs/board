import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Notice(models.Model):
    """
    Model representing a notice or post.

    Attributes:
        - title (`str`): The title of the notice.
        - content (`str`): The content or body of the notice.
        - publish_date (`datetime`): The date and time when the notice was published, automatically set to the current date and time.
        - author (`User`): The user who authored the notice. This is a foreign key to the `User` model, automatically set to the current user.
        - slug (`UUID`): A unique identifier for the notice, automatically generated.
    """
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
