from django.db import models



class Paciente(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dpi = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=8) 
    correo = models.EmailField()
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class Meta:
        db_table = 'Pacientes'

class Medico(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dpi = models.CharField(max_length=13, unique=True)
    numero_colegiado = models.CharField(max_length=7, unique=True)
    especialidad = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=8)  
    correo = models.EmailField()
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.numero_colegiado}"
    
    class Meta:
        db_table = 'Medicos'

class Cita(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    servicio = models.CharField(max_length=100)
    fecha_cita = models.DateTimeField()
    hora_cita = models.TimeField()

    URGENCIA = 'U'
    PROGRAMADA = 'P'
    TIPO_CONSULTA_CHOICES = [
        (URGENCIA, 'Urgente'),
        (PROGRAMADA, 'Programada'),
    ]
    tipo_consulta = models.CharField(
        max_length=1,
        choices=TIPO_CONSULTA_CHOICES,
        default=PROGRAMADA,
    )

    def atender_cita(self):
        self.estado = self.ESTADO_REALIZADA
        self.save()

    def reagendar_cita(self, nueva_fecha):
        self.estado = self.ESTADO_REAGENDADA
        self.fecha_cita = nueva_fecha
        self.save()

    def es_urgente(self):
        return self.tipo_consulta == self.URGENCIA


    def save(self, *args, **kwargs):
        self.nombre_paciente = self.paciente.nombre
        self.apellido_paciente = self.paciente.apellido
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.paciente} {self.servicio} {self.tipo_consulta} "
    
    class Meta:
        db_table = 'Cita'

class AtencionCita(models.Model):
    cita = models.OneToOneField('Cita', on_delete=models.CASCADE)
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
    diagnostico = models.TextField(max_length=1000)
    receta = models.TextField(max_length=1000)

    def __str__(self):
        return f"Atención de {self.cita.paciente} ({self.cita.servicio}) por {self.medico}"

    class Meta:
        db_table = 'AtencionCita'

    def save(self, *args, **kwargs):
        if self.cita:  # Verifica si existe una cita asociada
            self.nombre_paciente = self.cita.paciente.nombre
            self.apellido_paciente = self.cita.paciente.apellido

        if self.medico:  # Verifica si existe un médico asociado
            self.nombre_medico = self.medico.nombre
            self.apellido_medico = self.medico.apellido

        super().save(*args, **kwargs)