from .import views


from django.urls import path

urlpatterns = [
    path('', views.index, name='posts'),
    path('create', views.post_create, name='create'),

 
    ]
