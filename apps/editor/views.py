from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from forms import EditorForm
from models import Editor
# Create your views here.


def editor_list(request):
    editores = Editor.objects.all()
    return render(request,'editor/list.html',{'editores':editores})


def editor_create(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('editor:function_list')
    else:
        form = EditorForm()
        return render(request, 'editor/form.html', {'form':form})


def editor_update(request, pk):
    editor = Editor.objects.get(id=pk)
    if request.method == 'POST':
        form = EditorForm(request.POST, instance=editor)
        if form.is_valid():
            form.save()
        return redirect('editor:function_list')
    else:
        form = EditorForm(instance=editor)
        return render(request, 'editor/form.html', {'form': form})


def editor_delete(request, pk):
    editor = Editor.objects.get(id=pk)
    if request.method == 'POST':
        editor.delete()
        return redirect('editor:function_list')
    else:
        return render(request, 'editor/delete.html')


class EditorList(ListView):
    model = Editor
    template_name = 'editor/class/list.html'

class EditorCreate(CreateView):
    model = Editor
    template_name = 'editor/form.html'
    form_class = EditorForm
    success_url = reverse_lazy('editor:class_list')

class EditorUpdate(UpdateView):
    model = Editor
    template_name = 'editor/form.html'
    form_class = EditorForm
    success_url = reverse_lazy('editor:class_list')

class EditorDelete(DeleteView):
    model = Editor
    template_name = 'editor/class/delete.html'
    success_url = reverse_lazy('editor:class_list')