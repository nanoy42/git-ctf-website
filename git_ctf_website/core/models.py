from django.db import models


class Start(models.Model):
    time = models.DateTimeField(auto_now_add=True)


class Winner(models.Model):
    name = models.CharField(max_length=255)
    end_time = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True)
