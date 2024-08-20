from django.urls import path
from ageapp import views

urlpatterns = [
    path('age_input/', views.age_input),
    path('age_check/', views.age_check),
    path('adult/', views.adult),
    path('underage/', views.underage),

]