# python_learning_project
Desmistificando o Python.
O aplicativo usará um banco de dados SQLite para armazenar usuários e postagens. 
Python vem com suporte embutido para SQLite no módulo sqlite3. 
O SQLite é conveniente porque não requer a configuração de um servidor de banco de dados separado e é integrado ao Python. 
No entanto, se as solicitações simultâneas tentarem gravar no banco de dados ao mesmo tempo, elas ficarão mais lentas à medida que cada gravação ocorrer sequencialmente. 
Aplicativos pequenos não perceberão isso. 
Depois de se tornar grande, você pode querer mudar para um banco de dados diferente.

## CRIANDO, IMPORTANDO E CONFIGURANDO O PROJETO
1 - Criação do repositório no github.
```
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in
```

2 - Importação do projeto com git clone
```
$ git clone https://github.com/lucioweb/python_learning_project.git
```

3 - Alternando para a pasta do projeto clonado
```
$ cd python_learning_project
```

4 - Abrindo a pasta do projeto com o VSCode
```
$ code .
```

5 - Criando o venv na pasta do projeto
```
$ python3 -m venv .venv
```

6 - Ativando o venv (Conforme https://flask.palletsprojects.com/en/2.3.x/installation/) 
```
$ . .venv/bin/activate
```

7 - Criando o arquivo de manifesto `requirements.txt`.
Em vez de instalar pacotes individualmente, pip permite que você declare todas as dependências em um Arquivo de Requisitos. 
Por exemplo, você pode criar um arquivo `requirements.txt` na raiz do projeto, contendo todas as bibliotecas que deseja instalar:
```
$ python3 -m pip install -r requirements.txt
```

8 - Com a lib do Flask instalada no projeto, o comando será: `$ flask --app flaskr run`
```
$ flask --app flaskr run --debugger (Faz o debug e o reload do código)
```

## BANCO DE DADOS
1 - Inicializando o Banco de dados sqlite: `$ flask --app flaskr run`. 
Após isso será criado um arquivo chamdo `flaskr.sqlite` na *instance* do projeto.  
```
$ flask --app flaskr init-db
```











#### CAMINHO ONDE O PYTHON ESTÁ INSTALADO
```
$ sudo whereis python3
python3: /usr/bin/python3 /usr/lib/python3 /etc/python3 /usr/share/python3 /usr/share/man/man1/python3.1.gz
```
#### INSTALANDO O GERENCIADOR DE PACOTES PIP
```
$ sudo apt-get install python-pip
```
#### VERIFICANDO A VERSÃO DO PIP
```
$ pip --version
```
#### CRIANDO O WORKSPACE
```
$ luciolemos@dev:~$ mkdir my_python_projects && cd $_
```
#### CRIANDO A PASTA DO PROJETO
```
$ luciolemos@dev:~/my_python_projects$ mkdir python_project_1 && cd $_
```
#### INSTALANDO O VENV
```
$ sudo apt install python3.10-venv
```




#### CONSOLE EM MODO INTERATIVO
Quando os comandos são lidos a partir do console, diz-se que o interpretador está em modo interativo. Nesse modo ele solicita um próximo comando através do prompt primário, tipicamente três sinais de maior (>>>); para linhas de continuação do comando atual, o prompt secundário padrão é formado por três pontos (...). O interpretador exibe uma mensagem de boas vindas, informando seu número de versão e um aviso de copyright antes de exibir o primeiro prompt:
```
$ python
Python 3.10.6 (main, May 29 2023, 11:10:38) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
### Qual significado de GCC?
O GNU Compiler Collection (chamado usualmente por GCC) é um conjunto de compiladores de linguagens de programação produzido pelo projecto GNU para construir um sistema operativo semelhante ao Unix livre.


### Executando com o comando `$ python3 app.py`
```
$ python3 app.py
```

### Com a lib do Flask instalada no projeto, o comando será: `$ flask --app flaskr run`
```
$ flask --app flaskr run --debugger (Faz o debug e o reload do código)
```

### BANCO DE DADOS sqlite: `$ flask --app flaskr run`. Após isso será criado um arquivo chamdo `flaskr.sqlite` na *instance* do projeto.  
```
$ flask --app flaskr init-db
```

### TUTORIAL https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/
