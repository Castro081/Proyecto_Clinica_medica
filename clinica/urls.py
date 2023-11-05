from django.urls import path
from .views import registro, inicio_sesion, index, home, edit_citas,eliminar_medico, eliminar_paciente, cerrar_sesion,edit_medico, edit_paciente ,eliminar_cita, contacto, historia, otros, list_atencion , atencion_detalle ,paciente_edit, form_medico, form_paciente, form_citas,list_cita, list_paciente, paciente_detalle, medico_detalle, list_medico, cita_detalle,form_atencion ,modificar_cita

urlpatterns = [
    path('',index, name='index'),
    path('registro/',registro, name='Registro'),
    path('inicio_sesion/',inicio_sesion, name='inicio_sesion'),
    path('logout/', cerrar_sesion, name='cerrar_sesion'),
    path('contacto/', contacto, name='contacto'),
    path('historia/',historia, name='historia'),
    path('otros/', otros, name='otros'),
    path('form_medico/', form_medico, name='form_medico'),
    path('form_paciente/', form_paciente, name='form_paciente'),
    path('form_citas/', form_citas, name='form_citas'),
    path('form_atencion/', form_atencion, name='form_atencion'),
    path('lis_cita/', list_cita, name='list_cita'),
    path('home/', home, name='home'),
    path('list_paciente/', list_paciente, name='list_paciente'),
    path('list_atencion/', list_atencion, name='list_atencion'),
    path('paciente_detalle/', paciente_detalle, name='paciente_detalle'),
    path('atencion_detalle/', atencion_detalle, name='atencion_detalle'),
    path('list_medico/', list_medico, name='list_medico'),
    path('medico_detalle/', medico_detalle, name='medico_detalle'),
    path('edit_paciente/<id>/', edit_paciente, name='edit_paciente'),
    path('edit_medico/<id>/', edit_medico, name='edit_medico'),
    path('cita_detalle/', cita_detalle, name='cita_detalle'),
    path('edit_medico/', edit_medico, name='edit_medico'),
    path('edit_paciente/', edit_paciente, name='edit_paciente'),
    path('eliminar_paciente/<int:paciente_id>/', eliminar_paciente, name='eliminar_paciente'),
    path('eliminar_medico/<int:medico_id>/', eliminar_medico, name='eliminar_medico'),

]

