from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Tarefa
from django.db.models import Q

@login_required(login_url='/auth/login/')

def dashboard(request):
    # Verifica se a URL tem um pedido de filtro (ex: ?status=pendente)
    status_filtro = request.GET.get('status')

    # Busca as tarefas onde o usuário é criador ou responsável
    tarefas = Tarefa.objects.filter(
        Q(criador=request.user) | Q(atribuida_a=request.user)
    )

    # Se um filtro foi clicado, aplica ele na busca
    if status_filtro:
        tarefas = tarefas.filter(status=status_filtro)

    # Enviamos também o status_filtro para o HTML saber qual botão deixar "marcado"
    return render(request, 'dashboard.html', {
        'tarefas': tarefas, 
        'status_filtro': status_filtro
    })

@login_required(login_url='/auth/login/')
def nova_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        atribuida_id = request.POST.get('atribuida_a')

        tarefa = Tarefa(
            titulo=titulo,
            descricao=descricao,
            criador=request.user
        )

        if atribuida_id:
            tarefa.atribuida_a = User.objects.get(id=atribuida_id)
        else:
            tarefa.atribuida_a = request.user
            
        tarefa.save()
        return redirect('dashboard')

    usuarios = User.objects.all()
    return render(request, 'nova_tarefa.html', {'usuarios': usuarios})

@login_required(login_url='/auth/login/')
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    usuarios = User.objects.all()

    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.status = request.POST.get('status')
        atribuida_id = request.POST.get('atribuida_a')
        
        if atribuida_id:
            tarefa.atribuida_a = User.objects.get(id=atribuida_id)
        else:
            tarefa.atribuida_a = request.user
            
        tarefa.save()
        return redirect('dashboard')

    return render(request, 'editar_tarefa.html', {'tarefa': tarefa, 'usuarios': usuarios})

@login_required(login_url='/auth/login/')
def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('dashboard')