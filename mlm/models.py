from django.db import models


class Log(models.Model):
    """Model for logs"""
    path = models.URLField(max_length=200)
    method = models.CharField(max_length=4)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['timestamp', 'method']

    def __str__(self):
        return self.path
