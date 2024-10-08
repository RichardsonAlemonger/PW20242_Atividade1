from typing import List, Optional 
from models.usuario_model import Usuario
from sql.usuario_sql import SQL_CRIAR_TABELA, SQL_INSERIR, SQL_OBTER_TODOS
from util import obter_conexao

def criar_tabela():
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA)

def inserir(usuario: Usuario) -> Optional[Usuario]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_INSERIR, (
            usuario.nome,
            usuario.email,
            usuario.telefone,
            usuario.data_nascimento,
            usuario.senha
        ))

def obter_todos() -> List[Usuario]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        tuplas = db.execute(SQL_OBTER_TODOS).fetchall()
        usuarios = [Usuario(*t) for t in tuplas]
        return usuarios 