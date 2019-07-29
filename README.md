# My To Do

Aplicação web escrita usando **Python**, **Django** e **Bulma**, criada a fim de que usuários possam se registrar
e incluir coisas a fazer e controlar tais atividades.
Sendo possível determinar o status, a prioridade, data limite e cor para visualização do item.

## Tecnologias Usadas

* [Python v 3.7.3](https://www.python.org/)
* [Django v2.2.3](https://www.djangoproject.com/)
* [Bulma](https://bulma.io/)
* HTML5
* CSS
* JavaScript

## Iniciando a Aplicação

Na pasta *todo-django* instale os pacotes listados no arquivo *requirements.txt*:

`pip install -r requirements.txt`

Feito isso, crie as tabelas e as popule usando o comando:

`python manage.py migrate`

Crie um usuário no terminal para ter acesso ao painel administrativo do django:

`python manage.py createsuperuser`

Para rodar a aplicação execute o comando:

`python manage.py runserver`


## Componentes

O projeto é composto pelo app *core* que possui as funções de views e modelo relacionado ao *todo*. O projeto também 
contém os apps *colors*, *priorities*, *status* e *users* que lidam com as cores, prioridades, status e usuários, 
respectivamente.

O app *users* contém uma alteração para que o campo principal seja e-mail e não *username*. Para que isso tenha efeito,
a primeira migração a ser feita deve ser a do app *users* e depois as migrações básicas do Django.

A aplicação vem sem script para inclusão automática de cores, prioridades e status. Eles devem ser incluídos através do 
site admin oferecido pelo próprio Django.

## Páginas

- Cadastro
- Log in
- Lista de To Dos ainda sem status terminado
- Lista de To Dos com status terminado
- Página de inserção/edição de um To Do

As páginas foram feitas baseadas em um template comum. Portanto elas compartilham algumas seções como por exemplo, o 
*footer*.

## CSS

Para o design, foi utilizado Bulma, portanto a aplicação pode facilmente ser visualizada em smartphones e tablets. 


### Informações adicionais
O site pode ser visitado através do link <https://fdopradoarruda.pythonanywhere.com/>
Primeira versão 1.0
