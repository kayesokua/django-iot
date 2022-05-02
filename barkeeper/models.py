from django.db import models

# Create your models here.
class Event(models.Model):
    picamera_img = models.ImageField(upload_to='picamera',blank=True, null= True)
    picamera_img_url = models.URLField(blank=True, null=True)
    ocr_text = models.CharField(max_length=200,default='default')
    weight = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    result = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, editable=False)

    def __str__(self):
        return self.created

    def get_image_from_url(self, url): 
       #img_tmp = NamedTemporaryFile(delete=True)
       #with urlopen(url) as uo:
       #    assert uo.status == 200
       #    img_tmp.write(uo.read())
       #    img_tmp.flush()
       #img = File(img_tmp)
       #self.image.save(img_tmp.name, img)
       #self.image_url = url
       print("Return unique url path")
       return self.url