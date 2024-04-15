<h1><img src="static/img/logo.png" /> </h1>

## 📕 Sobre

Um site para consultar reserva dos laboratórios, podem ser feitas consultas por data e bloco ou pelo nome do professor e a data e registrar reservas

<!--ts-->
   * [Requisitos](#tabela-de-conteudo)
        * Ter instalado o python na versão 3.12

   * [Instalação](#instalacao)
        * Passo 1: clonar o respositório
        * Passo 2: na paste "ensalamento" criar um arquivo com o nome ".env"
        * Passo 3: coloar esse código no arquivo 
            * DB_NAME="nome do banco de dados"
            * DB_ROOT="usuario adminitrativo do banco de dados"
            * DB_HOST="endereço host"
            * DB_PORT="porta do banco de dados"
            * DB_USER="usuario do banco de dados"
            * DB_PASS="senha do usuario do banco de dados"
            * SECRET_KEY="chave secreta"
        * Passo 4: abrir o cmd na pasta raiz do projetor
        * Passo 5: executar o comando pipenv install pipfile
        * Passo 6: executar o comando pipenv shell
        * Passo 7: executar o comando py manage.py migrate
        * Passo 8: executar o comando py manage.py runserver    
   
   * [Tecnologias](#tecnologias)
        * Python
        * Djando
<!--te-->