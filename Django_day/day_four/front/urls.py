from django.urls import path

from front import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('find/', views.find, name="find"),
    path('update/', views.update, name="update"),
    path('delete/', views.delete, name="delete")

]