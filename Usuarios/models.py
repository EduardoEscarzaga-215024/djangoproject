from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(username, password, **extra_fields)

# Modelo personalizado
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    es_recepcionista = models.BooleanField(default=False)
    es_psicologo = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class Recepcionista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'Recepcionista: {self.user.get_username}'

class Psicologo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    tipo_servicio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo

class Paciente(models.Model):
    nombre_completo = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre_completo

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    motivo = models.TextField(blank=True)
    estado = models.CharField(max_length=50, choices=[
        ('Agendada', 'Agendada'),
        ('Cancelada', 'Cancelada'),
        ('Asistida', 'Asistida'),
    ], default='Agendada')

    def __str__(self):
        return f'{self.paciente} - {self.fecha_hora.strftime("%d/%m/%Y %H:%M")}'



    