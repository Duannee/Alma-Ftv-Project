# Alma Ftv
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Duannee/Alma-Ftv-Project/blob/main/LICENSE) 

# Sobre o projeto


Alma-Ftv é um API rest para gerenciamento de centros de treinamento de futvolei. A API foi desenvolvida em Python usando Django e Django Rest Framework.
A Alma-Ftv API é uma ferramenta que ajuda os donos dos centros de treinamento a organizarem e controlarem as atividades do negócio de forma simples e eficiente.
Com ela, é possível gerenciar as informações dos estudantes, acompanhar os pagamentos, e administrar os técnicos que trabalham no CT.

## Base URL
A URL base para acessar a API é:

## Funcionalidades
- `Contas`: CRUD completo para contas de usuários.
- `Estudantes`: Gerenciamento de estudantes, incluindo a criação, leitura, atualização e exclusão.
- `Perfis de Estudantes`: Cada estudante pode ter um perfil detalhado associado a ele.
- `Pagamentos`: Controle de pagamentos realizados pelos estudantes com um perfil de pagamento associado a cada estudante, facilitando o controle.
- `Treinadores`: Gerenciamento de informações dos treinadores do CT.

## Requisitos
- Python 3.8+
- Django 4.0+
- Django Rest Framework 3.12+
- drf-spectacular 0.22+

## Instalação
Clone o repositório:
``` bash
git clone https://github.com/Duannee/Alma-Ftv-Project
cd nome-do-repositorio
```
Crie um ambiente virtual:
``` bash
python3 -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```
Instale as dependências:
```bash
pip install -r requirements.txt
```
Execute as migrações:
```bash
python manage.py migrate
```
Crie um superusuário para acessar o admin:
```bash
python manage.py createsuperuser
```
Inicie o servidor:
```bash
python manage.py runserver
```

# Autenticação
Esta API usa autenticação para os métodos POST, PATCH, PUT e DELETE. Para acessar essas funcionalidades, é necessário incluir um token de autenticação no cabeçalho das requisições.

## Como obter o token de autenticação

### Obter o token:
- Com o superusuário que foi criado 
- Faça login usando o endpoint `/api/token/`. 
- Você receberá um token JWT que deverá ser usado para autenticar as solicitações subsequentes.

### Obter Refresh Token: 
Seu token expira em 30 minutos, e então você precisa gerar ele novamente caso deseje fazer uma nova requisição após ter expirado.
- No endpoint `/api/token/` copie a chave `refresh`.
- No endpoint `/api/token/refresh/` cole o seu `refresh` no corpo da requisição e então seu novo token será gerado como resposta.

## Endpoints
A documentação completa dos endpoints da API pode ser acessada após iniciar o servidor em 
- [Documentação Alma-Ftv-API](http://127.0.0.1:8000/api/docs/alma/)

### Exemplos de Endpoints
- POST `/api/user/create/` - Criar todas as contas.
- GET `/api/student/list/` - Listar todos os alunos.
- GET `/api/student_profile/{id}/retrieve/` - Retorna detalhes de um perfil de um aluno específico.
- PATCH `/api/payment/{id}/update/` - Atualiza os dados de pagamento de um aluno.
- DELETE `/api/coach/{id}/delete/` - Exclui um técnico.

# Tecnologias utilizadas
- Python
- Django
- Django Rest Framework


# Autor

Duanne Moraes de Souza 

[Duanne Moraes Linkedin](https://www.linkedin.com/in/duanne-moraes-7a0376278/)

