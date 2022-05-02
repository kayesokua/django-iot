from rest_framework import serializers
from barkeeper.models import Event
import pytesseract
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

class EventSerializer(serializers.ModelSerializer):
    ocr_text = serializers.SerializerMethodField

    class Meta:
        model = Event
        exclude = ('created')

    def get_ocr_text(self,object):
        oct_image = object.image
        ocr_text = pytesseract.image_to_string(oct_image)
        return ocr_text