from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm


# LISTA
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'app_proyectos/lista_proyectos.html', {'proyectos': proyectos})

# CREATE
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'app_proyectos/crear_proyecto.html', {'form': form})

# UPDATE
def editar_proyecto(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, id_proyecto=id_proyecto)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'app_proyectos/editar_proyecto.html', {'form': form, 'proyecto': proyecto})

# DELETE
def eliminar_proyecto(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, id_proyecto=id_proyecto)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'app_proyectos/eliminar_proyecto.html', {'proyecto': proyecto})

# READ DETAIL
def ver_proyecto(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, id_proyecto=id_proyecto)
    return render(request, 'app_proyectos/ver_proyecto.html', {'proyecto': proyecto})