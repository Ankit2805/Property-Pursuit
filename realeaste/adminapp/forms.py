from django.forms import ModelForm
from . import models
from django import forms
class detailsform(ModelForm):
    class Meta:
        model = models.property
        fields = "__all__"
        widget = {
            'p_direction': forms.RadioSelect()
        }

class updateform(ModelForm):
    class Meta:
        model = models.property
        fields = "__all__"

class MyImageForm(forms.ModelForm):
    class Meta:
        model = models.MyImage
        fields = ['image']