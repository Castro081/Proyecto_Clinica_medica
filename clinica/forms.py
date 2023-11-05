# forms.py
from django.contrib.auth.models import User
from django import forms
from .models import Paciente, Cita, Medico, AtencionCita



class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'servicio', 'fecha_cita', 'hora_cita', 'tipo_consulta']

    def __init__(self, *args, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)

        # Personaliza el queryset del campo 'paciente' para mostrar los pacientes almacenados
        self.fields['paciente'].queryset = Paciente.objects.all()
        paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(), empty_label="Selecciona un paciente")
class AtencionCitaForm(forms.ModelForm):
    class Meta:
        model = AtencionCita
        fields = ['cita', 'medico', 'diagnostico', 'receta']
        widgets = {
            'cita': forms.Select(attrs={'class': 'form-select', 'readonly': 'readonly'}),
            'medico': forms.Select(attrs={'class': 'form-select', 'readonly': 'readonly'}),
        }

