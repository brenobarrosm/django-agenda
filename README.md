<h1 style="color: #8E007E">📔 Agenda de Contatos</h1>

### **❓ O que é?**

Este projeto consiste em um website para exibir contatos telefônicos, por meio de uma página inicial, contendo paginação
e a opção de buscar pelo nome de um contato em específico.

É possível criar uma conta para acessar uma dashboard privada. Dentro desta área, é possível criar novos contatos, que serão exibidos para outras pessoas na página inicial.

<br>

### **🛠 Como funciona?**

![Gif mostrando funcionalidades da página](GIF_Agenda.gif)

No site, existem as seguintes áreas que podem ser acessadas executando o servidor localmente:
* **Página inicial:** São exibidos todos os contatos existentes na base de dados.
* **Dashboard:** Área destinada à criação de novos contatos para serem exibidos a dashboard. Pode ser acessada fazendo com login com um usuário já existente, caso contrário, também é possível registrar um novo usuário

<br>

### **⌨️ Como rodar o projeto no seu computador?**

1. Primeiramente é necessário fazer a instalação das dependências necessário utilizando o seguinte comando na pasta raiz do projeto:

```bash
pip install -r requirements.txt
```

2. Agora execute o seguinte comando no terminal:

```bash
python manage.py runserver
```

Agora o servidor vai começar a rodar localmente na porta 8000, podendo ser acessado no navegador utilizando [localhost:8000](localhost:8000).

<br>

### **💻 Principais tecnologias utilizadas**
* [Python 3](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [SQLite 3](https://www.sqlite.org/index.html)

    #### **Outras tecnologias:**

    * [HTML 5](https://www.w3schools.com/html/default.asp)
    * [CSS 3](https://www.w3schools.com/css/)
    * [Boostrap](https://getbootstrap.com/)
    * [Pillow](https://pillow.readthedocs.io/en/stable/)

