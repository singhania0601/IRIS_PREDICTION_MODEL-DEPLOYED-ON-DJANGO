from django.contrib import admin
from django.urls import path,include
from predict import views

app_name = "predict"
urlpatterns = [
  path('',views.predict,name="predict"),
   path('predict/', views.predict_chances, name='submit_prediction'),
   path('results/', views.view_results, name='results'),
]