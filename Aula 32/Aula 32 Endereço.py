# pip3 install flask_mysqldb
# referencia ao Mysql

import MySQLdb


#listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM tb_pessoa')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)

#buscar uma pessoa pelo ID
def buscar_por_id(c, id_pessoa):
    c.execute(f'SELECT * FROM tb_pessoa WHERE ID = {id_pessoa}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM tb_pessoa WHERE SOBRENOME like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)

#salvar pessoa
def salvar(cn, cr, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"INSERT INTO tb_pessoa (NOME, SOBRENOME, IDADE, ENDERECO_ID )VALUES('{nome}', '{sobrenome}',{idade},{endereco_id})")
    cn.commit()

#alterar pessoa
def alterar(cn, cr, id_pessoa, nome, sobrenome, idade, endereco_id='NULL'):
    try:
        cr.execute(f"UPDATE tb_pessoa SET NOME='{nome}', SOBRENOME='{sobrenome}', IDADE={idade}, ENDERECO_ID={endereco_id} WHERE ID_pessoa={id_pessoa} ")
        cn.commit()
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        if(e.args[0]==1452):
            print(f"Erro de Foreign Key jovem, id errado")

#deletar pessoa por ID
def deletar(cn, cr, id_pessoa):
    cr.execute(f'DELETE FROM tb_pessoa WHERE ID_pessoa ={id_pessoa}')
    cn.commit()

conexao = MySQLdb.connect(host='localhost', database='aula_bd2', user='root', passwd='')
cursor = conexao.cursor()

# listar_todos(cursor)
# buscar_por_id(cursor, 3)
# buscar_por_sobrenome(cursor,'Gru')
# salvar(conexao, cursor, 'Voltolini', 'KingOfFlask', 16,5)
alterar(conexao, cursor, 8, 'Gugu Voltolini', 'KingOfBasquete', 17, 6)
# deletar(conexao, cursor, 7)