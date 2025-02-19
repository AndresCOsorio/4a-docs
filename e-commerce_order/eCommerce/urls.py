"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eCommerceApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orderDetail/<int:user>/', views.order_detail_view, name="order_detail_view"),
    path('orderDetail/<int:user>/<int:pk>/', views.order_detail2_view, name="order_detail2_view"),
    path('orderDetail/<int:user>/<int:pk>/<int:product>/', views.order_detail3_view, name="order_detail3_view"),
    path('order/<int:user>/', views.order_view, name="order_view"),
    path('order/<int:user>/<int:pk>/', views.detail_order_view, name="detail_order_view"),
]
