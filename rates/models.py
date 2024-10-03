"""Database models for the rates app"""

import uuid
from django.db import models

class Rates(models.Model):
    """Represents a rate in the database"""

    rate_id = models.UUIDField(
        verbose_name = "rate_id",
        primary_key = True,
        default = uuid.uuid4,
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
    rate_validated = models.BooleanField(
        verbose_name = "rate_validated",
        default = False,
        help_text = "If the email was validated or not, see the user flow diagram",
    )
    rate_campus_id = models.ForeignKey(
        verbose_name = "rate_campus_id",
        to = "Campuses",
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
        help_text = "Unique identifier for the university",
    )
    university_name = models.CharField(
        verbose_name = "university_name",
        max_length = 255,
        help_text = "Name of the university",
    )
    university_website = models.CharField(
        verbose_name = "university_website",
        max_length = 255,
        help_text = "Url of the university website",
    )

class Campuses(models.Model):
    """Represent a university campus"""

    campus_id = models.IntegerField(
        verbose_name = "campus_id",
        primary_key = True,
        help_text = "Unique identifier for the campus",
    )
    campus_university_id = models.ForeignKey(
        verbose_name = "campus_university_id",
        to = "Universities",
        on_delete = models.CASCADE,
    )
    campus_name = models.CharField(
        verbose_name = "campus_name",
        max_length = 255,
        help_text = (
            "Name of the campus, if it own only one campus it "
            "should be null, filled if more than one exists"
        ),
    )
    campus_country = models.CharField(
        verbose_name = "campus_country",
        max_length = 255,
        help_text = (
            "Country of the campus in ISO 3166-1 name format, "
            "see more in https://en.wikipedia.org/wiki/ISO_3166-1"
        ),
    )
    campus_state = models.CharField(
        verbose_name = "campus_state",
        max_length = 255,
        help_text = "State of the campus",
    )
    campus_city = models.CharField(
        verbose_name = "campus_city",
        max_length = 255,
        help_text = "City of the campus",
    )
