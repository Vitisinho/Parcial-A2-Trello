# Gerenciador de Tarefas 📋


Uma aplicação web simples e responsiva desenvolvida em **Python** e **Django** para o gerenciamento colaborativo de tarefas. O sistema conta com autenticação de usuários, atribuição de atividades e suporte nativo a Modo Escuro (Dark Mode).


## ✨ Funcionalidades


- **Autenticação:** Cadastro de usuários e login customizado utilizando e-mail.
- **CRUD de Tarefas:** Crie, edite, visualize e exclua tarefas rapidamente.
- **Colaboração:** Atribua tarefas a você mesmo ou a outros membros da equipe.
- **Filtros Dinâmicos:** Filtre o dashboard instantaneamente por status (Pendente, Em Andamento, Concluída).
- **Interface e Acessibilidade:** Design responsivo com Bootstrap 5 e botão de Dark/Light mode integrado.


## 🚀 Como rodar o projeto localmente


Siga os passos abaixo para configurar e executar a aplicação na sua máquina:


**1. Preparação**
Clone este repositório ou extraia os arquivos em uma pasta local. Em seguida, abra o terminal na raiz do projeto.


**2. Ambiente Virtual (.venv)**
É recomendado o uso de um ambiente virtual. Crie com o comando:
> `python -m venv .venv`


Ative o ambiente virtual:
- **No Windows:** `.\.venv\Scripts\activate`
- **No Linux/Mac:** `source .venv/bin/activate`


**3. Instalação de Dependências**
Com o ambiente ativado `(.venv)`, instale o Django:
> `pip install django`


**4. Servidor e Banco de Dados**
O banco de dados SQLite (`db.sqlite3`) já vem pré-configurado. Basta iniciar o servidor local:
> `python manage.py runserver`


**5. Acesso**
Abra o navegador e acesse a aplicação em: [http://127.0.0.1:8000/auth/login/](http://127.0.0.1:8000/auth/login/)


---


## 💻 Como usar o sistema


1. **Primeiro Acesso:** Clique em "Cadastre-se" para criar uma nova conta no sistema.
2. **Dashboard:** O painel central exibe todas as tarefas atreladas a você (criadas por você ou atribuídas a você). Utilize os botões do topo para filtrar a visualização por status.
3. **Nova Tarefa:** Clique em `+ Nova Tarefa`, adicione título, descrição e defina quem será o responsável por ela.
4. **Atualizar Tarefa:** Utilize o botão `Editar` para mudar o status de uma atividade. As cores das etiquetas mudarão automaticamente.
5. **Excluir:** O botão `Excluir` apaga a tarefa permanentemente do banco de dados (uma confirmação será solicitada para evitar exclusões acidentais).


---
**Desenvolvido por:** Matheus Eduardo Ducati e Vitor Marcelo Barzick Nogueira