from django.urls import path
from exapp import views

urlpatterns = [
    path('01/', views.func01),
    path('02/', views.func02),
    path('03/', views.func03),
    path('04/', views.func04),
    path('05/', views.func05),
    path('06/', views.func06),
    path('07/', views.func07),
    path('08/', views.func08),
    path('09/', views.func09),
]