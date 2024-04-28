from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/<int:service_id>/', views.service_detail,
         name='service_detail'),
    path('create/', views.service_create, name='service_create'),
    path('services/<int:service_id>/edit', views.service_edit,
         name='service_edit'),
    path('services/<int:service_id>/order', views.to_order, name='to_order'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/<int:order_id>/status', views.change_order_status,
         name='change_order_status')
]
