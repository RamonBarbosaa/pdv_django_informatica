# 💻 PDV Informática - Sistema de Gestão de Vendas

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## 🛒 Sobre o Projeto
O **PDV Informática** é uma solução robusta de Ponto de Venda desenvolvida para simplificar a gestão de pequenas e médias assistências técnicas e lojas de produtos de informática. O sistema foca na agilidade do processo de checkout e no controle preciso do fluxo de mercadorias.

> **Objetivo:** Oferecer uma interface administrativa intuitiva para controle total sobre vendas, estoque e cadastro de clientes.

## 🛠️ Funcionalidades
* **Gestão de Estoque:** Controle de entrada e saída de componentes (SSD, Memória RAM, Periféricos).
* **Fluxo de Vendas:** Registro de transações com cálculo automático de subtotal e total.
* **Módulo de Clientes:** Cadastro completo para histórico de compras e fidelização.
* **Painel Administrativo:** Interface customizada do Django para gerenciamento rápido de dados.
* **Relatórios de Saída:** Visualização clara de quais itens foram vendidos e quando.

## 🏗️ Arquitetura Técnica
O projeto utiliza o padrão **MVT (Model-View-Template)** do Django, garantindo uma separação clara entre a lógica de banco de dados e a interface do usuário.

* **Models:** Estrutura de dados normalizada para evitar redundância.
* **Views:** Processamento de requisições e lógica de fechamento de carrinho.
* **Templates:** Interface responsiva e limpa.

---

## 🚀 Como Executar

### 1. Preparar o ambiente
```bash
# Clone o repositório
git clone [https://github.com/RamonBarbosaa/pdv_django_informatica.git](https://github.com/RamonBarbosaa/pdv_django_informatica.git)
cd pdv_django_informatica

# Crie e ative o ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

. Instalar dependências

pip install django

3. Rodar as migrações e o servidor

python manage.py migrate
python manage.py runserver
Acesse: http://127.0.0.1:8000
