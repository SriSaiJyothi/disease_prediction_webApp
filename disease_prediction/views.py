from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import disease,DiabetesPrediction,HeartDiseasePrediction,ParkinsonsDiseasePrediction,HepatitisDieasePrediction
import joblib
# Create your views here.
#import joblib 
# Load the joblib models
import sklearn
import os 

#diabetes_model = joblib.load(r'disease_prediction\joblib\my_model(RegressionImputationShuffledModified).joblib')
"""heart_disease_model = joblib.load('disease_prediction_app\joblibes_files\heart_model.sav')
parkinsons_model = joblib.load('disease_prediction_app\joblibes_files\parkinson_model.sav')
"""
from .forms import DiabetesPredictionForm,HeartDiseasePredictionForm,ParkinsonsDiseasePredictionForm,HepatitisDieasePredictionForm
def index(request):
      diseases=disease.objects.all()
      return render(request,'index.html',{'diseases':diseases})
    #disease_list=  disease.objects.all()
    #template=loader.get_template("disease_prediction/index.html") 
    #context={
    #     "disease":disease_list,}
  
 
    #return HttpResponse(template.render(context,request))
def disease_form(request,disease_id):
      disease_instance=get_object_or_404(disease,pk=disease_id)
      print(f'disease_instance:{disease_instance}')
      form_mapping={
            'diabetes':(DiabetesPredictionForm,'diabetes_prediction'),
            'heart disease':(HeartDiseasePredictionForm,'heart_disease_prediction'),
            'parkinsons disease':(ParkinsonsDiseasePredictionForm,'parkinsons_disease_prediction'),
            'hepatitis':(HepatitisDieasePredictionForm,'Hepatitis_disease_prediction')
      }
      form_class,redirect_view_name=form_mapping.get(disease_instance.disease_name.lower(),(None,None))
      if form_class is None or redirect_view_name is None:
            return HttpResponse("No form found for the given disease.")
      if request.method =='POST':
         form=form_class(request.POST)
           ## form=DiabetesPredictionForm(request.POST)
         if form.is_valid():
                  instance=form.save()
                  return redirect(redirect_view_name,prediction_instance_id=instance.pk)
            
      else:
            form=form_class()

      return render(request,'disease_prediction_form.html',{'form':form,'disease':disease_instance})

import numpy as np
file_path='disease_prediction\joblib\diabetes_model.joblib'
parkinsons_file_path='disease_prediction\joblib\parkinsons_model.joblib'

parkinsons_model=joblib.load(parkinsons_file_path)
hepatitis_file_path='disease_prediction\joblib\model_hepatitis.joblib'
hepatitis_model=joblib.load(hepatitis_file_path)
heart_file_path='disease_prediction\joblib\heart_disease_model_xgboost.joblib'
heart_disease_model=joblib.load(heart_file_path)
print(os.getcwd())

if os.path.exists(file_path):
      diabetes_model=joblib.load(file_path)
else:
      print(f"Error:File not found at {file_path}")
def diabetes_prediction(request,prediction_instance_id):

        instance=DiabetesPrediction.objects.get(pk=prediction_instance_id)

        # Handle form submission
        Glucose = float(instance.Glucose)
        Insulin = float(instance.Insulin)
        BMI=float(instance.BMI)
        Age=float(instance.Age)
        scaler=joblib.load('disease_prediction\joblib\scaler.joblib')
        input_data=np.array([[Glucose,Insulin,BMI,Age]])
        
        print("Scikit-learn version during fitting:", sklearn.__version__)
        input_data_re=input_data.reshape(1,-1)
        new_data_scaled = scaler.transform(input_data_re)
        # Use the diabetes machine learning model for prediction
        
        print("Scikit-learn version during fitting:", sklearn.__version__)

        prediction = diabetes_model.predict(new_data_scaled)
        if prediction[0] == 1:
               diabetes_result="The model predicts that patient is diabetic."
        else:
               diabetes_result="The model predicts that patient is Non-diabetic."
        # Render a template to display the results
        return HttpResponse(diabetes_result)

   


def heart_disease_prediction(request,prediction_instance_id):
        instance_heart=HeartDiseasePrediction.objects.get(pk=prediction_instance_id)
        # Handle form submission
        age = int(instance_heart.age)
        sex = int(instance_heart.sex)
        cp=int(instance_heart.cp)
        trestbps=int(instance_heart.trestbps)
        chol=int(instance_heart.chol)
        fbs=int(instance_heart.fbs)
        restecg=int(instance_heart.restecg)
        thalach=int(instance_heart.thalach)
        exang=int(instance_heart.exang)
        oldpeak=float(instance_heart.age)
        slope=int(instance_heart.slope)
        ca=int(instance_heart.ca)
        thal=int(instance_heart.thal)
        scaler_heart=joblib.load('disease_prediction\joblib\scaler1_heart.joblib')
        # Use the heart disease machine learning model for prediction
        heart_disease = np.asarray([age, sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        heart_disease=heart_disease.reshape(1,-1)
        heart_disease_scaled=scaler_heart.transform(heart_disease)
        heart_disease_result=heart_disease_model.predict(heart_disease_scaled)
        if heart_disease_result[0] == 1:
               heart_disease_result="The model predicts that patient have heart disease."
        else:
               heart_disease_result="The model predicts that patient doesnt have heart disease."
        # Render a template to display the results
        return HttpResponse(heart_disease_result)

def parkinsons_disease_prediction(request,prediction_instance_id):
   instance_parkinsons=ParkinsonsDiseasePrediction.objects.get(pk=prediction_instance_id)

        # Handle form submission
   mdvp_fo = float(instance_parkinsons.mdvp_fo)
   mdvp_fhi = float(instance_parkinsons.mdvp_fhi)
   mdvp_flo= float(instance_parkinsons.mdvp_flo)
        
   mdvp_jitter_p=float(instance_parkinsons.mdvp_jitter_p)
   mdvp_jitter_abs=float(instance_parkinsons.mdvp_jitter_abs)
   mdvp_rap=float(instance_parkinsons.mdvp_rap)
   mdvp_ppq=float(instance_parkinsons.mdvp_ppq)
   jitter_ddp =float(instance_parkinsons.jitter_ddp)
   mdvp_shimmer =float(instance_parkinsons.mdvp_shimmer)
   mdvp_shimmer_db=float(instance_parkinsons.mdvp_shimmer_db)
   shimmer_apq3=float(instance_parkinsons.shimmer_apq3)
   shimmer_apq5=float(instance_parkinsons.shimmer_apq5)
   mdvp_apq=float(instance_parkinsons.mdvp_apq)
   shimmer_dda=float(instance_parkinsons.shimmer_dda)
   nhr=float(instance_parkinsons.nhr)
   hnr=float(instance_parkinsons.hnr)
   rpde=float(instance_parkinsons.rpde)
   dfa=float(instance_parkinsons.dfa)
   spread1=float(instance_parkinsons.spread1)
   spread2=float(instance_parkinsons.spread2)
   d2=float(instance_parkinsons.d2)
   ppe=float(instance_parkinsons.ppe)
   scaler_parkin=joblib.load('disease_prediction\joblib\scaler_parkinsons.joblib')
   input_data=np.array([mdvp_fo, mdvp_fhi, mdvp_flo ,mdvp_jitter_p, mdvp_jitter_abs,mdvp_rap,mdvp_ppq,jitter_ddp, mdvp_shimmer ,mdvp_shimmer_db,shimmer_apq3,shimmer_apq5,mdvp_apq, shimmer_dda,nhr, hnr,rpde,dfa,spread1, spread2,d2,ppe])
   input_data_reshaped=input_data.reshape(1,-1)
   input_scaled=scaler_parkin.transform(input_data_reshaped)
        # Use the Parkinson's disease machine learning model for prediction
   parkinsons = parkinsons_model.predict(input_scaled)
   if parkinsons[0] == 1:
               parkinsons_result="The model predicts that patient have parkinsons."
   else:
               parkinsons_result="The model predicts that patient doesn't have parkinsons."
        # Render a template to display the results
   return HttpResponse(parkinsons_result)
    
def Hepatitis_disease_prediction(request,prediction_instance_id):
            instance_hepatitis=HepatitisDieasePrediction.objects.get(pk=prediction_instance_id)
            age =int(instance_hepatitis.age)                
            sex  =int(instance_hepatitis.sex)               
            steroid  =int(instance_hepatitis.steroid)           
            antivirals=int(instance_hepatitis.antivirals)          
            fatigue    =int(instance_hepatitis.fatigue)         
            malaise   =int(instance_hepatitis.malaise)          
            anorexia  =int(instance_hepatitis.anorexia)          
            liver_big   =int(instance_hepatitis.liver_big)        
            liver_firm   =int(instance_hepatitis.liver_firm)       
            spleen_palable =int(instance_hepatitis.spleen_palable)     
            spiders =int(instance_hepatitis.spiders)            
            ascites  =int(instance_hepatitis.ascites)           
            varices   =int(instance_hepatitis.varices)          
            bilirubin =float(instance_hepatitis.bilirubin) 
            alk_phosphate=float(instance_hepatitis.alk_phosphate)         
            sgot  =int(instance_hepatitis.sgot)      
            albumin =float(instance_hepatitis.albumin)         
            protime =int(instance_hepatitis.protime)            
            histology =int(instance_hepatitis.histology) 
            input_data_hepatitis= np.asarray([age,sex,steroid,antivirals,fatigue,malaise,anorexia,liver_big,liver_firm,spleen_palable,spiders,ascites,varices,bilirubin,alk_phosphate,sgot,albumin,protime,histology])   
            scaler_hepatitis=joblib.load('disease_prediction\joblib\scaler_hepatitis.joblib')
            input_data_hepatitis_reshape=input_data_hepatitis.reshape(1,-1)
            input_data_hepatitis_scaled=scaler_hepatitis.transform(input_data_hepatitis_reshape)
            hepatitis=hepatitis_model.predict(input_data_hepatitis_scaled)
            if hepatitis[0] == 1:
                   hepatitis_result="The model predicts that patient doesnt have hepatitis."
            else:
                   hepatitis_result="The model predicts that patient  have hepatitis."
            return HttpResponse(hepatitis_result)
                   

      