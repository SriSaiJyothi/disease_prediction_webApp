from django.db import models

# Create your models here.
class disease(models.Model):
    disease_name=models.CharField(max_length=200)
    def __str__(self):
        return self.disease_name
class DiabetesPrediction(models.Model):
    Glucose = models.FloatField()
    Insulin = models.FloatField()
    BMI =models.FloatField()
    Age=models.IntegerField()
    # Add other fields relevant to diabetes prediction

class HeartDiseasePrediction(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    cp=models.IntegerField()
    trestbps=models.IntegerField()
    chol=models.IntegerField()
    fbs=models.IntegerField()
    restecg=models.IntegerField()
    thalach=models.IntegerField()
    exang=models.IntegerField()
    oldpeak=models.FloatField()
    slope=models.IntegerField()
    ca=models.IntegerField()
    thal=models.IntegerField()

    # Add other fields relevant to heart disease prediction

class ParkinsonsDiseasePrediction(models.Model):
    mdvp_fo = models.FloatField()
    mdvp_fhi = models.FloatField()
    mdvp_flo=models.FloatField()
    mdvp_jitter_p =models.FloatField()
    mdvp_jitter_abs=models.FloatField()
    mdvp_rap= models.FloatField()
    mdvp_ppq= models.FloatField()
    jitter_ddp = models.FloatField()
    mdvp_shimmer= models.FloatField()
    mdvp_shimmer_db=models.FloatField()
    shimmer_apq3=models.FloatField()
    shimmer_apq5=models.FloatField()
    mdvp_apq=models.FloatField()
    shimmer_dda=models.FloatField()
    nhr=models.FloatField()
    hnr=models.FloatField()
    rpde=models.FloatField()
    dfa=models.FloatField()
    spread1=models.FloatField()
    spread2=models.FloatField()
    d2=models.FloatField()
    ppe=models.FloatField()
    
    
class HepatitisDieasePrediction(models.Model):
    
        age =models.IntegerField()               
        sex =models.IntegerField()              
        steroid =models.IntegerField()           
        antivirals  =models.IntegerField()       
        fatigue  =models.IntegerField()          
        malaise =models.IntegerField()           
        anorexia  =models.IntegerField()         
        liver_big   =models.IntegerField()       
        liver_firm   =models.IntegerField()      
        spleen_palable =models.IntegerField()    
        spiders  =models.IntegerField()     
        ascites  =models.IntegerField()          
        varices =models.IntegerField()         
        bilirubin =models.FloatField()  
        alk_phosphate=models.FloatField()           
        sgot =models.IntegerField()        
        albumin  =models.FloatField()         
        protime =models.IntegerField()           
        histology =models.IntegerField()  
    # Add other fields relevant to Parkinson's disease prediction
