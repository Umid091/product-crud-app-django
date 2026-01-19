from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/',views.detail,name='detail'),
    path('create/', views.create, name='create_product'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]