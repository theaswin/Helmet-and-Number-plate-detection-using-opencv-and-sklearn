from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('getPath',views.getPath,name='getPath'),
    # path('saveToDb',views.saveToDb,name='saveToDb')



]
