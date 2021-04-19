from django.db import models


class LabReportStatusChoice(models.TextChoices):
    READY_TO_SEND_LAB = "Ready to send lab"
    IN_QUEUE = "Queue"
    START_PROCESSING = "Start Processing"
    COMPLETED = "Complete"
