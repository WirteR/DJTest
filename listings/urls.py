from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('test', views.for_lab1, name='test'),
    path('test2', views.for_lab2, name='test2'),
    path('test3', views.for_lab3, name='test3'),
    path('test4', views.for_lab4, name='test4')

]