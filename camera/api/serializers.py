from rest_framework import serializers
from camera.models import PiImage
import pytesseract

class PiImageSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    ocr_text = serializers.SerializerMethodField

    class Meta:
        model = PiImage
        exclude = ('created')

    def get_ocr_text(self,object):
        oct_image = object.image
        ocr_text = pytesseract.image_to_string(oct_image)
        return ocr_text
        
    def get_image_url(self, object):
        return self.context['request'].build_absolute_uri(object.image.url)