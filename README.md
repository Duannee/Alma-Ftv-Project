# Big Game Survey 
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Duannee/Alma-Ftv-Project/blob/main/LICENSE) 

# About Project


Alma-Ftv é um API rest para gerenciamento de centros de treinamento de futvolei. 
A API para o CTs de futevôlei é uma ferramenta que ajuda os donos do centro de treinamento a organizarem e controlarem as atividades do negócio de forma simples e eficiente.
Com ela, é possível gerenciar as informações dos estudantes, acompanhar os pagamentos, e administrar os técnicos que trabalham no CT.

## Base URL
A URL base para acessar a API é:

# Autenticação
Método de Autenticação
A API utiliza autenticação baseada em tokens. Cada usuário autenticado deve incluir um token de autenticação em cada requisição.

Exemplo de Requisição
Para autenticar e consumir um endpoint protegido:
``` bash
curl -H "Authorization: Bearer <seu_token_aqui>" https://api.meuct.com.br/v1/estudantes/
```

3. Endpoints
Contas
<ul>GET /contas/ - Lista todas as contas.</ul>
<ul>POST /contas/ - Cria uma nova conta.</ul>
<ul>GET /contas/{id}/ - Detalha uma conta específica.</ul>
<ul>PUT /contas/{id}/ - Atualiza uma conta.</ul>
<ul>DELETE /contas/{id}/ - Exclui uma conta.</ul>
Estudantes
<ul>GET /estudantes/ - Lista todos os estudantes.</ul>
<ul>POST /estudantes/ - Cria um novo estudante.</ul>
<ul>GET /estudantes/{id}/ - Detalha um estudante específico.</ul>
<ul>PUT /estudantes/{id}/ - Atualiza um estudante.</ul>
<ul>DELETE /estudantes/{id}/ - Exclui um estudante.</ul>
Perfis de Estudantes
<ul>GET /perfis/ - Lista todos os perfis de estudantes.</ul>
<ul>POST /perfis/ - Cria um novo perfil de estudante.</ul>
<ul>GET /perfis/{id}/ - Detalha um perfil de estudante específico.</ul>
<ul>PUT /perfis/{id}/ - Atualiza um perfil de estudante.</ul>
<ul>DELETE /perfis/{id}/ - Exclui um perfil de estudante.</ul>
Pagamentos
<ul>GET /pagamentos/ - Lista todos os pagamentos.</ul>
<ul>POST /pagamentos/ - Cria um novo pagamento.</ul>
<ul>GET /pagamentos/{id}/ - Detalha um pagamento específico.</ul>
<ul>PUT /pagamentos/{id}/ - Atualiza um pagamento.</ul>
<ul>DELETE /pagamentos/{id}/ - Exclui um pagamento.</ul>
Técnicos
<ul>GET /tecnicos/ - Lista todos os técnicos.</ul>
<ul>POST /tecnicos/ - Cria um novo técnico.</ul>
<ul>GET /tecnicos/{id}/ - Detalha um técnico específico.</ul>
<ul>PUT /tecnicos/{id}/ - Atualiza um técnico.</ul>
<ul>DELETE /tecnicos/{id}/ - Exclui um técnico.</ul>



# Tecnologias utilizadas
## Back end
- Python
- Django Rest Framework

## Implantação em produção
- Back end: Render
- Banco de dados: Postgresql

# Como executar o projeto



# Autor

Duanne Moraes de Souza 

https://www.linkedin.com/in/duanne-moraes-7a0376278/

