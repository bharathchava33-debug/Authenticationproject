from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.home),
    path('register/',views.home),
    path('javaex/',views.java),
    path('pythonex/',views.python),
    path('uiex/',views.ui),
    path('signup/',views.register),
    path('logout/',views.logout_view,name='logout'),


]