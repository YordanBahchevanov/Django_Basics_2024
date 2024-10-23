from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import AlphaNumericValidator


class Profile(models.Model):
    username = models.CharField(
        max_length =15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator(),
        ]
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )