from django import forms
from Usuarios.models import Cita, Paciente, Psicologo

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'psicologo', 'fecha_hora', 'motivo', 'estado']
        widgets = {'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
                   'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                   }