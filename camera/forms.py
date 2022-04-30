from django.forms import ModelForm
from .models import PiImage

class PiImageForm(ModelForm):
    class Meta:
        model = PiImage
        fields = '__all__'