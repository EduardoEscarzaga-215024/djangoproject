from django.shortcuts import render, redirect
from Usuarios.models import Cita
from Citas.forms import CitaForm

# Create your views here.
def agendar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'Citas/agendar_cita.html', {'form': form})
