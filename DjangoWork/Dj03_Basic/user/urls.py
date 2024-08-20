from django.urls import path, include
from user import views

urlpatterns = [
    # path(url pattern, view함수)   # url 에 매핑할 view 함수 지정.
    path('', views.index),

    # 여러 url 을 하나의 view 함수에 매핑할수도 있다.
    path('aaa/', views.index),
    path('aaa/bbb/', views.index),
    path('aaa/bbb/ccc/', views.index),

    path('user/list/', views.list),
    path('user/detail/4/', views.detail),
    path('user/update/', views.update),
]