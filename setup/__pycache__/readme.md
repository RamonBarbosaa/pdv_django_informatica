🛒 PDV Tech - Sistema de Frente de Caixa para Informática
Este é um sistema de Ponto de Venda (PDV) desenvolvido com Django, focado em lojas de equipamentos de informática. O projeto simula uma operação real de frente de caixa com foco em segurança e performance.

🚀 Funcionalidades Principais
Interface Estilo Cupom: Design clássico de nota fiscal que organiza os itens em tempo real.

Busca Dinâmica: Pesquisa rápida de produtos.

Proteção de Estoque: Validação no Back-end que impede vendas de itens sem estoque.

Segurança de Acesso: Uso de @login_required para proteger rotas.

Pronto para Impressão: Layout otimizado para impressoras térmicas.

📦 Como rodar o projeto (Passo a Passo)

1. Clonar o Repositório
Abra o terminal e digite:
git clone https://www.google.com/search?q=https://github.com/SEU_USUARIO/pdv-django-informatica.git

2. Configurar o Ambiente Virtual (VENV)
python -m venv venv

Ativar o ambiente:

Windows: .\venv\Scripts\activate

Linux/Mac: source venv/bin/activate

3. Instalar as Dependências
pip install django

4. Preparar o Banco de Dados
python manage.py makemigrations
python manage.py migrate

5. Criar Usuário Administrador
python manage.py createsuperuser

6. Iniciar o Servidor
python manage.py runserver

Agora acesse: http://127.0.0.1:8000/produtos/

👤 Autor
Ramon Barbosa - desenvolvedor web Full Stack