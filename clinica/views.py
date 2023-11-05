
from venv import logger
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.contrib import messages
from django.db import IntegrityError
from .forms import CitaForm, PacienteForm, AtencionCitaForm, MedicoForm
from .models import Paciente, Medico, Cita, AtencionCita
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_POST

# ---------------------------------------------------------------------------------------------#
# -----------------------------------------Vistas----------------------------------------------#
def contacto(request):
    return render(request, 'contacto.html')

def historia(request):
    return render(request, 'historia.html')

def otros(request):
    return render(request, 'otros.html')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='inicio_sesion')  
def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registro.html', {"form": UserCreationForm, "error": "El nombre de Usuario ya esta registrado."})
        return render(request, 'registro.html', {"form": UserCreationForm, "error": "Contraseña no coinciden."})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            return render(request, 'inicio_sesion.html', {"form": form, "error": "El usuario o la contraseña son incorrectos."})
    else:
        form = AuthenticationForm()
        return render(request, 'inicio_sesion.html', {"form": form})
    

# -----------------------------------------Logins----------------------------------------------#
# ---------------------------------------Formularios-------------------------------------------#
# ------------------------------------Formularios Medico---------------------------------------#
def form_medico(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dpi = request.POST.get('dpi')
        numero_colegiado = request.POST.get('numero_colegiado')
        especialidad = request.POST.get('especialidad')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        genero = request.POST.get('genero')
        medico = Medico(
            nombre=nombre,
            apellido=apellido,
            dpi=dpi,
            numero_colegiado=numero_colegiado,
            especialidad=especialidad,
            fecha_nacimiento=fecha_nacimiento,
            telefono=telefono,
            correo=correo,
            genero=genero
        )
        medico.save()

        messages.success(request, 'Médico registrado exitosamente.')
        return redirect('home')  

    return render(request, 'form_medico.html')

def list_medico(request):
    return render(request, 'list_medico.html')

def medico_detalle(_request):
    medicos = list(Medico.objects.values())
    data = {'Medico':medicos}
    return JsonResponse(data)

def edit_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    if request.method == 'POST':
        formulario = MedicoForm(data=request.POST, instance=medico)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='list_medico')
    else:
        formulario = MedicoForm(instance=medico)

    data = {'form': formulario}
    return render(request, 'edit_medico.html', data)

@login_required
def eliminar_medico(request, medico_id):
    medico = get_object_or_404(Medico, id=medico_id)
    medico.delete()
    return JsonResponse({'mensaje': 'Médico eliminado exitosamente'})
# -----------------------------------Formularios Paciente--------------------------------------#

def form_paciente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dpi = request.POST.get('dpi')
        direccion = request.POST.get('direccion')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        genero = request.POST.get('genero')
        paciente = Paciente(
            nombre=nombre,
            apellido=apellido,
            dpi=dpi,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            telefono=telefono,
            correo=correo,
            genero=genero
            
        )
        paciente.save()
        return redirect('home')

    return render(request, 'form_paciente.html')


def paciente_detalle(_request):
    pacientes = list(Paciente.objects.values())
    data = {'Pacientes':pacientes}
    return JsonResponse(data)

def edit_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == 'POST':
        formulario = PacienteForm(data=request.POST, instance=paciente)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='list_paciente')
    else:
        formulario = PacienteForm(instance=paciente)

    data = {'form': formulario}
    return render(request, 'edit_paciente.html', data)

def list_paciente(request):
    return render(request, 'list_paciente.html')

@login_required
def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    paciente.delete()
    return JsonResponse({'mensaje': 'Paciente eliminado exitosamente'})
# -------------------------------------Formularios Cita----------------------------------------#

def form_citas(request):
    pacientes = Paciente.objects.all()
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('home')
    else:
        form = CitaForm()

    return render(request, 'form_citas.html', {'form': form, 'pacientes': pacientes})

def edit_citas(request, id):
    cita = get_object_or_404(Cita, id=id)

    if request.method == 'POST':
        formulario = CitaForm(data=request.POST, instance=cita)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='list_cita')
    else:
        formulario = CitaForm(instance=cita)

    data = {'form': formulario}
    return render(request, 'edit_citas.html', data)


def list_cita(request):
    return render(request, 'list_cita.html')


def cita_detalle(_request):
    try:
        citas = Cita.objects.all()
        citas_data = [
            {
                'nombre_paciente': cita.paciente.nombre if cita.paciente else 'N/A',
                'apellido_paciente': cita.paciente.apellido if cita.paciente else 'N/A',
                'servicio': cita.servicio,
                'fecha_cita': cita.fecha_cita,
                'hora_cita': cita.hora_cita,
                'tipo_consulta': cita.tipo_consulta,
            }
            for cita in citas
        ]

        data = {'Citas': citas_data}
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)})
    



# -------------------------------------Formularios Atencion------------------------------------------#

def form_atencion(request):
    if request.method == 'POST':
        form = AtencionCitaForm(request.POST)
        if form.is_valid():
            try:
                cita_id = form.cleaned_data['cita']
                medico_id = form.cleaned_data['medico']
                diagnostico = form.cleaned_data['diagnostico']
                receta = form.cleaned_data['receta']

                cita = get_object_or_404(Cita, id=cita_id.id if hasattr(cita_id, 'id') else cita_id)
                medico = get_object_or_404(Medico, id=medico_id.id if hasattr(medico_id, 'id') else medico_id)

                atencion_cita = AtencionCita.objects.filter(cita=cita, medico=medico).first()

                if atencion_cita:
                    atencion_cita.diagnostico = diagnostico
                    atencion_cita.receta = receta
                    atencion_cita.save()
                    messages.success(request, 'Datos de AtencionCita actualizados correctamente.')
                else:

                    AtencionCita.objects.create(
                        cita=cita,
                        medico=medico,
                        diagnostico=diagnostico,
                        receta=receta,
                    )
                    messages.success(request, 'Datos de AtencionCita guardados correctamente.')

                return redirect('home')

            except Exception as e:
                print("Error al guardar datos. Excepción:", str(e))
                messages.error(request, 'Error al guardar datos. Por favor, revisa los datos ingresados.')

        else:
            print("Formulario no válido:", form.errors)
            messages.error(request, 'Error en el formulario. Por favor, revisa los campos.')

    else:
        form = AtencionCitaForm()

    citas = Cita.objects.all()
    medicos = Medico.objects.all()

    return render(request, 'form_atencion.html', {'form': form, 'citas': citas, 'medicos': medicos})

def atencion_detalle(request):
    try:
        atenciones = AtencionCita.objects.all()
        atenciones_data = []

        for atencion in atenciones:
            atencion_info = {
                'nombre_paciente': atencion.cita.paciente.nombre if atencion.cita.paciente else 'N/A',
                'apellido_paciente': atencion.cita.paciente.apellido if atencion.cita.paciente else 'N/A',
                'nombre_medico': atencion.medico.nombre if atencion.medico else 'N/A',
                'apellido_medico': atencion.medico.apellido if atencion.medico else 'N/A',
                'diagnostico': atencion.diagnostico,
                'receta': atencion.receta,
            }
            atenciones_data.append(atencion_info)

        data = {'AtencionCita': atenciones_data}
        
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': 'No se pudieron recuperar los datos.'})
    
    
def list_atencion(request):
    return render(request, 'list_atencion.html')