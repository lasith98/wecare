from django.db import models


class DurationTextChoice(models.TextChoices):
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
