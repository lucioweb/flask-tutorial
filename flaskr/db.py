import sqlite3
import click
from flask import current_app, g

# sqlite3.connect()estabelece uma conexão com o arquivo apontado pela chave "DATABASE" de configuração.
# Esse arquivo ainda não precisa existir e não existirá até que o banco de dados seja inicializado.


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

# Inicializando o banco de dados


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# flask --app flaskr init-db, inicializa a base de dados.


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Base de dados inicializada com sucesso!')

# close_db () verifica se uma conexão foi criada, verificando se g.db foi definida.
# Se a conexão existir, ela será fechada.


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
