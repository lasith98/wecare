from django.db import models


class TimeChoice(models.TextChoices):
    DAY = "Day"
    NIGHT = "Night"
    MORNING = "Morning"
    FULL_DAY = "Full Day"
