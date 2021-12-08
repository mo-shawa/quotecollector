from django.forms import ModelForm
from .models import Fan

class FanForm(ModelForm):
    class Meta:
        model = Fan
        fields = '__all__'