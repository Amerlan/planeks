from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        "Created date",
        auto_now_add=True, blank=True,
    )

    updated_at = models.DateTimeField(
        "Modified date",
        auto_now=True, blank=True,
    )

    @property
    def pretty_update_at(self):
        return f"{self.updated_at}".split('.')[0]
