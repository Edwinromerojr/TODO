from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('update_list/<str:pk>/', views.updateList, name="update_list"),
    path('delete_list/<str:pk>/', views.deleteList, name="delete_list"),

]