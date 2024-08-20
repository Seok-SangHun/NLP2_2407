from django.urls import include, path
from params import views

urlpatterns = [
    path('page1/', views.page1),
    path('page2/', views.page2),
]