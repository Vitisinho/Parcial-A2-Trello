from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    
    # Quem criou a tarefa
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas_criadas')
    # Para quem a tarefa foi delegada (pode ficar em branco se for para a própria pessoa)
    atribuida_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefas_atribuidas')
    
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo