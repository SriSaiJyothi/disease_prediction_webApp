from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('disease/<int:disease_id>/',views.disease_form,name="disease_form"),
    path('diabetes_prediction/<int:prediction_instance_id>/', views.diabetes_prediction, name='diabetes_prediction'),
    path('heart_disease_prediction/<int:prediction_instance_id>/', views.heart_disease_prediction, name='heart_disease_prediction'),
    path('parkinsons_disease_prediction/<int:prediction_instance_id>/', views.parkinsons_disease_prediction, name='parkinsons_disease_prediction'),
    path('Hepatitis_disease_prediction/<int:prediction_instance_id>/',views.Hepatitis_disease_prediction,name='Hepatitis_disease_prediction'),
]