from django.urls import path
from . import views


urlpatterns = [
    #index
    path('', views.servicios, name='metodoPago'),
    path('success/', views.payment_success, name='payment-success'),
    path('failure/', views.payment_failure, name='payment-failure'),
    path('selmetodopago', views.selmetodopago, name='selmetodopago'),
    path('crearEmpresapago/', views.crearEmpresapago, name='crearEmpresapago'),
    path('OrdenDeCompra/', views.OrdenDeCompra, name='OrdenDeCompra'),
    path('GenerarOrdenDeCompra/', views.GenerarOrdenDeCompra, name='GenerarOrdenDeCompra'),
    path('generarPDF/', views.generarPDF, name='generarPDF'),



]