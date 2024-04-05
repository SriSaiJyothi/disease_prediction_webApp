# myapp/forms.py

from django import forms
from .models import DiabetesPrediction,HeartDiseasePrediction,ParkinsonsDiseasePrediction,HepatitisDieasePrediction

class DiabetesPredictionForm(forms.ModelForm):
    class Meta:
        model = DiabetesPrediction
        fields = ['Glucose','Insulin','BMI','Age']  # Add other fields as needed

class HeartDiseasePredictionForm(forms.ModelForm):
    class Meta:
        model=HeartDiseasePrediction
        fields=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']

class ParkinsonsDiseasePredictionForm(forms.ModelForm):
    class Meta:
        model=ParkinsonsDiseasePrediction
        fields=['mdvp_fo','mdvp_fhi','mdvp_flo','mdvp_jitter_p','mdvp_jitter_abs','mdvp_rap','mdvp_ppq','jitter_ddp','mdvp_shimmer','mdvp_shimmer_db','shimmer_apq3','shimmer_apq5','mdvp_apq','shimmer_dda','nhr','hnr','rpde','dfa','spread1','spread2','d2','ppe']
class HepatitisDieasePredictionForm(forms.ModelForm):
    class Meta:
        model=HepatitisDieasePrediction
        fields=['age','sex','steroid','antivirals','fatigue','malaise','anorexia','liver_big','liver_firm','spleen_palable','spiders','ascites','varices','bilirubin','alk_phosphate','sgot','albumin','protime','histology' ]
         