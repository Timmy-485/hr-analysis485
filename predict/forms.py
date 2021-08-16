from django import forms
from .models import PredictionResults

class PredictCreateForm(forms.ModelForm):
    class Meta:
        model = PredictionResults
        # fields = ('__all__')
        exclude = ['prediction_result']