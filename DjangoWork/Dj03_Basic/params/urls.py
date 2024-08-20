from django.urls import include, path
from params import views

urlpatterns = [
    path('page1/', views.page1),
    path('page2/', views.page2),

    # URL 에 담긴 값 받기
    path('article1/<year>/', views.article1),

    # path converter 명시 가능
    path('article2/<int:year>/<int:month>/', views.article2),

]