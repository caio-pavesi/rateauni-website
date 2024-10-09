"""Database models for the rates app"""

import uuid
from django.db import models

class Rates(models.Model):
    """Represents a rate in the database"""

    rate_id = models.UUIDField(
        verbose_name = "rate_id",
        primary_key = True,
        default = uuid.uuid4,
    )
    rate_date = models.DateTimeField(
        verbose_name = "rate_date",
        auto_now_add = True,
        help_text = "Creation date of the rate",
    )
    rate_email = models.CharField(
        verbose_name = "rate_email",
        max_length = 255,
        null = True,
        help_text = "Email of the user who rated, 'NULL' if skipped validation",
    )
    rate_validated = models.BooleanField(
        verbose_name = "rate_validated",
        default = False,
        help_text = "If the email was validated or not, see the user flow diagram",
    )
    rate_university_id = models.ForeignKey(
        verbose_name = "rate_university_id",
        to = "Universities",
        on_delete = models.DO_NOTHING,
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
    )
    university_source_id = models.CharField(
        verbose_name = "university_source_id",
        max_length = 255,
        help_text = (
            "Unique identifier for the university in the source data "
            "usually the source API or the data provider (e.g: government)"
        ),
    )
    university_name = models.CharField(
        verbose_name = "university_name",
        max_length = 255,
        help_text = "Name of the university",
    )
    university_acronym = models.CharField(
        verbose_name = "university_acronym",
        max_length = 255,
        null = True,
        help_text = (
            "Acronym of the university e.g: 'MIT' for 'Massachusetts Institute of Technology'"
        ),
    )
    university_country = models.CharField(
        verbose_name = "university_country",
        max_length = 255,
        help_text = "Country of the university in ISO 3166-1 name (English) format",
    )
    university_state = models.CharField(
        verbose_name = "university_state",
        max_length = 255,
        null = True,
        help_text = (
            "State of the university, middle for the contry to in "
            "ISO 3166-2 or as definied by the source data"
        ),
    )
    university_city = models.CharField(
        verbose_name = "university_city",
        max_length = 255,
        help_text = (
            "City of the university, lower for the contry to in "
            "ISO 3166-2 or as definied by the source data"
        ),
    )
