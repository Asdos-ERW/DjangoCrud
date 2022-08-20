from django.db import models

class kegiatan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.name