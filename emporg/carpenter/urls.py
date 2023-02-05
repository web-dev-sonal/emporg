from django.urls import path, include
# from django.conf.urls import url
from carpenter import views

urlpatterns = [
    path('',views.showList,name='carpenter-list'),
    path('editList/',views.editList),
    path('deleteList/',views.deleteList),
    path('addList/',views.addList),
    path('add/',views.add),
    path('edit/',views.edit),
    path('viewProfile/',views.viewProfile),

]
