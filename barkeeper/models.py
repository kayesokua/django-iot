from django.db import models

# Create your models here.
class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    text = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    result = models.BooleanField(default=False)

    def __str__(self):
        return self.created