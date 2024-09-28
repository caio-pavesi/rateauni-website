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
    rate_university_id = models.ForeignKey(
        to = "Universities",
        on_delete = models.CASCADE,
    )
    rate_value = models.IntegerField(
        verbose_name = "rate_value",
        help_text = "Value of the rate",
    )

class Universities(models.Model):
    """Represents a university in the database"""

    university_id = models.IntegerField(
        verbose_name = "university_id",
        primary_key = True,
        help_text = "Unique identifier for the university",
    )
    university_name = models.CharField(
        verbose_name = "university_name",
        max_length = 255,
        help_text = "Name of the university",
    )
    university_campus = models.CharField(
        verbose_name = "university_campus",
        max_length = 255,
        help_text = "Campus of the university",
    )
    university_country = models.CharField(
        verbose_name = "university_country",
        max_length = 255,
        help_text = "Country of the university",
    )
    university_state = models.CharField(
        verbose_name = "university_state",
        max_length = 255,
        help_text = "State of the university",
    )
    university_city = models.CharField(
        verbose_name = "university_city",
        max_length = 255,
        help_text = "City of the university",
    )
