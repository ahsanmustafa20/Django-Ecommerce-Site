from django.urls import path
from shop import views

urlpatterns = [
    path('', views.ProductList.as_view(), name = 'index'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('success/', views.Success.as_view(), name='success')
]
