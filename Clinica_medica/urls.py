"""
URL configuration for Clinica_medica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from clinica import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('registro/',views.registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('registro/',views.registro, name='registro'),
    path('logout/',views.cerrar_sesion, name='cerrar_sesion'),
    path('contacto/',views.contacto, name='contacto'),
    path('historia/', views.historia, name='historia'),
    path('otros/', views.otros, name='otros'),
    path('form_medico/', views.form_medico, name='form_medico'),
    path('form_paciente/', views.form_paciente, name='form_paciente'),
    path('form_citas/', views.form_citas, name='form_citas'),
    path('list_cita/', views.list_cita, name='list_cita'),
    path('form_atencion/', views.form_atencion, name='form_atencion'),
    path('home/', views.home, name='home'),
    path('list_paciente/', views.list_paciente, name='list_paciente'),
    path('list_medico/', views.list_medico, name='list_medico'),
    path('list_atencion/', views.list_atencion, name='list_atencion'),
    path('paciente_detalle/', views.paciente_detalle, name='paciente_detalle'),
    path('medico_detalle/', views.medico_detalle, name='medico_detalle'),
    path('atencion_detalle/', views.atencion_detalle, name='atencion_detalle'),
    path('edit_paciente/<id>/', views.edit_paciente, name='edit_paciente'),
    path('cita_detalle/', views.cita_detalle, name='cita_detalle'),
    path('edit_paciente/', views.edit_paciente, name='edit_paciente'),
    path('edit_medico/<id>/', views.edit_medico, name='edit_medico'),
    path('edit_medico/', views.edit_medico, name='edit_medico'),
    path('eliminar_paciente/<int:paciente_id>/', views.eliminar_paciente, name='eliminar_paciente'),
    path('eliminar_medico/<int:medico_id>/', views.eliminar_medico, name='eliminar_medico'),

]
