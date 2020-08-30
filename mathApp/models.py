from django.db import models
from django import forms
from django.urls import reverse
from djongo import models as modelsDjongo

class Calculate(modelsDjongo.Model):
    number1 = modelsDjongo.SmallIntegerField()
    number2 = modelsDjongo.SmallIntegerField()
    total = modelsDjongo.SmallIntegerField()

# class CalculateCreateForm(forms.ModelForm):
#     number1 = forms.IntegerField()
#     number2 = forms.IntegerField()
#     class Meta:
#         model = Calculate
#         fields = ('number1', 'number2')

# class CalculateResult(forms.ModelForm):
#     total = forms.IntegerField()
#     class Meta:
#         model = Calculate
#         fields = ('total',)