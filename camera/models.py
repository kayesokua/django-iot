from django.db import models
from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

class PiImage(models.Model):
    picamera_img = models.ImageField(upload_to='picamera',blank=True, null= True,)
    ocr_text = models.CharField(max_length=200,default='default')
    created = models.DateTimeField(auto_now_add=True,editable=False)
    picamera_img_url = models.URLField(blank=True, null=True)
    
    def get_image_from_url(self, url):
       img_tmp = NamedTemporaryFile(delete=True)
       with urlopen(url) as uo:
           assert uo.status == 200
           img_tmp.write(uo.read())
           img_tmp.flush()
       img = File(img_tmp)
       self.image.save(img_tmp.name, img)
       self.image_url = url

    def __str__(self):
        return self.created