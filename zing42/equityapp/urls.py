from django.urls import path
from django.urls import re_path
from equityapp import views

urlpatterns = [
    #re_path('', views.home,name='home'),
    #path('category/show/<char:id>',views.categorydisplay,name="categorydisplay"),
    #re_path('category/',views.categorylisting,name="categorylisting"),
    path('', views.home, name="categorylisting"),
    path('category/', views.categorylisting, name="categorylisting"),
    path('category/create', views.categorycreate, name="categorycreate"),
    path('category/delete', views.categorydelete, name="categorydelete"),

]
