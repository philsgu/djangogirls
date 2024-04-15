from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #this directs initial site to post_list
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
