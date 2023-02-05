from django.urls import path, include
# from django.conf.urls import url
from home import views

urlpatterns = [
    path('carpenter/',include('carpenter.urls')),
    path('driver/',include('driver.urls')),
    path('electrician/',include('electrician.urls')),
    path('servant/',include('home_servant.urls')),
    path('painter/',include('painter.urls')),
    path('teacher/',include('teacher.urls')),
    path('about/',views.about),
    path('contact/',views.contact),
    path('Login/',views.Login),
    path('',views.home_page),
]
