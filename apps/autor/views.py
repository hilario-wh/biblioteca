from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from models import Autor
from forms import AutorForm

# Create your views here.


def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'autor/list.html', {'autores': autores})


def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor:function_list')
    else:
        form = AutorForm()
        return render(request, 'autor/form.html', {'form':form})


def autor_update(request, pk):
    autor = Autor.objects.get(id=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
        return redirect('autor:function_list')
    else:
        form = AutorForm(instance=autor)
        return render(request, 'autor/form.html', {'form': form})


def autor_delete(request, pk):
    autor = Autor.objects.get(id=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('autor:function_list')
    else:
        return render(request, 'autor/delete.html', {'autor': autor})


class AutorList(ListView):
    model = Autor
    template_name = 'autor/class/list.html'


class AutorCreate(CreateView):
    model = Autor
    template_name = 'autor/form.html'
    form_class = AutorForm
    success_url = reverse_lazy('autor:class_list')

class AutorUpdate(UpdateView):
    model = Autor
    template_name = 'autor/form.html'
    form_class = AutorForm
    success_url = reverse_lazy('autor:class_list')

class AutorDelete(DeleteView):
    model = Autor
    template_name = 'autor/class/delete.html'
    success_url = reverse_lazy('autor:class_list')