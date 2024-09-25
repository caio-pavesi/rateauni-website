"""Database models for the rates app"""

from django.db import models

class Rates(models.Model):
    """Represents a rate in the database"""

    rate_id = models.IntegerField(
        verbose_name = "rate_id",
        primary_key = True,
        help_text = "Unique identifier for the rate",
    )
    rate_date = models.DateTimeField(
        verbose_name = "rate_date",
        auto_now_add = True,
        help_text = "Creation date of the rate",
    )
    rate_email = models.CharField(
        verbose_name = "rate_email",
        max_length = 255,
        help_text = "Email of the user who rated, 'Anonymous' if skipped validation",
    )
    rate_value = models.IntegerField(
        verbose_name = "rate_value",
        help_text = "Value of the rate",
    )
