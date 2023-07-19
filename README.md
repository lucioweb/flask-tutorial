#### CAMINHO ONDE O PYTHON ESTÁ INSTALADO
```
$ sudo whereis python3
$ python3: /usr/bin/python3 /usr/lib/python3 /etc/python3 /usr/share/python3 /usr/share/man/man1/python3.1.gz
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
#### CRIANDO O VENV NA PASTA DO PROJETO
```
$ python3 -m venv env
```

#### ATIVANDO O VENV
```
$ source env/bin/activate
```

#### ABRINDO O PROJETO COM O VSCODE
```
$ code .
```

#### CRIANDO O ARQUIVO DE MANIFESTO `requirements.txt`
Em vez de instalar pacotes individualmente, pip permite que você declare todas as dependências em um Arquivo de Requisitos. Por exemplo, você pode criar um arquivo `requirements.txt` na raiz do projeto, contendo todas as bibliotecas que deseja instalar:
```
$ python3 -m pip install -r requirements.txt
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