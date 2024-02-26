from django.forms import ModelForm
from . import models
from django import forms
from dealerapp.models import property
class bookingform(ModelForm):
    class Meta:
        model = models.property
        fields = "__all__"
        exclude = ('user','prop',)