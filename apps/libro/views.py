from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from models import Libro
from forms import LibroForm

# Create your views here.
def index(request):
    return render(request, 'libro/index.html')


def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'libro/list.html', {'libros': libros})


def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('libro:function_list')
    else:
        form = LibroForm()
        return render(request, 'libro/form.html', {'form': form})


def libro_update(request, pk):
    libro = Libro.objects.get(id=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro:function_list')
    else:
        form = LibroForm(instance=libro)
        return render(request, 'libro/form.html', {'form': form})

def libro_delete(request, pk):
    libro = Libro.objects.get(id=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro:function_list')
    return render(request, 'libro/delete.html')


class LibroList(ListView):
    model = Libro
    template_name = 'libro/class/list.html'

class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/form.html'
    success_url = reverse_lazy('libro:class_list')

class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/form.html'
    success_url = reverse_lazy('libro:class_list')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'libro/class/delete.html'
    success_url = reverse_lazy('libro:class_list')