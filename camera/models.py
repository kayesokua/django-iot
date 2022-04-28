from django.db import models

class PiImage(models.Model):
    picamera_img = models.ImageField(upload_to='picamera',blank=True)
    ocr_text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.created