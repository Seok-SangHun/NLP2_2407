from django.urls import path
from board import views

urlpatterns = [
    path('write/', views.write),   # 작성 board/write/
    path('list/', views.list),    # 목록 board/list/ 
    path('detail/<int:id>/', views.detail),   # 상세 board/detail/id/
    path('update/<int:id>/', views.update),   # 수정 board/update/id/
    path('update/', views.update),   # 수정완료 board/update/
    path('delete/', views.delete),   # 삭제 board/delete/
]