from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefas
from .forms import TarefasForm

# Create your views here.
def listaTarefa(request):
    Tarefas_list = Tarefas.objects.all().order_by('-created_at')
    return render(request, 'tarefas/list.html', {'tarefas' :Tarefas_list})

def novaTarefa(request):
    if request.method == 'POST':
        form = TarefasForm(request.POST)
        form.save()
        return redirect('/')
     
    else:
        form = TarefasForm()
        return render(request, 'tarefas/addTarefa.html', {'form':form})

def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa':tarefa})