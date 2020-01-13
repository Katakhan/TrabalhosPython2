import MySQLdb

conexao = MySQLdb.connect(host='localhost',database='aula_bd2',user='root',passwd='' )
cursor = conexao.cursor()
def listar_todos(c):
    cursor.execute('SELECT * FROM tb_pessoa')
    pessoas = cursor.fetchall()
    for p in pessoas:
        print(p)

def buscar_por_id(c,id):
    c.execute(f'select * from tb_pessoa where id_tbpessoa = {id}')
    pessoas = c.fetchone()
    print(pessoas)

conexao = MySQLdb.connect(host='localhost', database='aula_bd2', user='root', passwd='')
cursor=conexao.cursor()

buscar_por_id(cursor,1)