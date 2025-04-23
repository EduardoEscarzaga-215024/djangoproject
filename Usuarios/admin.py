from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from Usuarios.models import User, Recepcionista, Psicologo, Paciente, Cita

# Register your models here.
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'es_recepcionista', 'es_psicologo', 'is_staff', 'is_superuser')
    list_filter = ('es_recepcionista', 'es_psicologo', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permisos', {'fields': ('es_recepcionista', 'es_psicologo', 'is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'es_recepcionista', 'es_psicologo', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(User)
admin.site.register(Recepcionista)
admin.site.register(Psicologo)
admin.site.register(Paciente)
admin.site.register(Cita)
