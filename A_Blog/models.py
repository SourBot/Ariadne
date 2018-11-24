from django.db import models

# Create your models here.
class memo(models.Model):
    title = models.CharField(max_length=60)
    message = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text
