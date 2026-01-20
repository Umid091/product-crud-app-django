from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    path('product/<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('create/', views.CreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete_product'),
]