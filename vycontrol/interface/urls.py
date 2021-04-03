from django.urls import path

from . import views

app_name = 'interface'

urlpatterns = [
    path('', views.index, name='interface-list'),
    path('interface-show/<slug:interface_type>/<str:interface_name>', views.interfaceshow, name='interface-show'),
    path('interface-firewall/<slug:interface_type>/<str:interface_name>', views.interfacefirewall, name='interface-firewall'),
    path('interface-set-firewall/<slug:interface_type>/<str:interface_name>', views.interface_set_firewall, name='interface-set-firewall'),
    path('interface-set/<slug:interface_type>/<str:interface_name>', views.interface_set, name='interface-set'),

]
