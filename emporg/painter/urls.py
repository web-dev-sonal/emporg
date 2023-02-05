from django.urls import path, include
# from django.conf.urls import url
from painter import views

urlpatterns = [
    path('',views.showList,name='painter-list'),
    path('editList/',views.editList),
    path('deleteList/',views.deleteList),
    path('addList/',views.addList),
    path('add/',views.add),
    path('edit/',views.edit),
    path('viewProfile/',views.viewProfile),
]
