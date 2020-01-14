import MySQLdb

#Listando Todos dados da tabela
def listar_todos(c):
    c.execute('SELECT * FROM tb_pessoa')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)

#Buscar pelo id
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM tb_pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#Buscar por Sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM tb_pessoa WHERE SOBRENOME like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)


#Salvar Pessoa
def salvar(cn,cr,Nome,SobreNome,Idade, endereco_id='NULL'):
    if endereco_id == None:
        endereco_id = 'NULL'
    cr.execute(f"INSERT INTO tb_pessoa (Nome,SobreNome,Idade,endereco_id) VALUES ('{Nome}', '{SobreNome}' , {Idade} , {endereco_id} ) ")
    cn.commit()

#Alterar Pessoa
def alterar(cn,cr,Id_pessoa,Nome,SobreNome,Idade, endereco_id='NULL'):
    cr.execute(f"UPDATE tb_pessoa SET Nome='{Nome}', Sobrenome='{SobreNome}' , Idade={Idade} , endereco_id={endereco_id}  WHERE Id_pessoa={Id_pessoa}")
    cn.commit()

#Deletar Pessoa
def deletar(cn, cr, Id_pessoa):
    cr.execute(f'DELETE FROM tb_pessoa WHERE Id_pessoa={Id_pessoa}')
    cn.commit()

conexao = MySQLdb.connect(host='localhost', database='aula_bd2', user='root', passwd='')
cursor= conexao.cursor()

#Comandos Para CRUD ;

# listar_todos(cursor)
# buscar_por_id(cursor, 2)
# buscar_por_sobrenome(cursor,'Sil')
# salvar(conexao,cursor,'Pablo','Cardoso',12,2)
# alterar(conexao,cursor, 3 ,'Rafaela','Mendes',18, 1)
# deletar(conexao,cursor,3)


#Listando Todos dados da tabela
def listar_todos(c):
    c.execute('SELECT * FROM tb_endereco')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)

#Buscar pelo id
def buscar_por_id(c, IDEndereco):
    c.execute(f'SELECT * FROM tb_endereco WHERE IDEndereco = {IDEndereco}')
    endereco = c.fetchone()
    print(endereco)

#Salvar Rua
def salvar(cn,cr,IDEndereco,Rua,bairro,cep):
    cr.execute(f"INSERT INTO tb_endereco (IDEndereco,Rua,bairro,cep) VALUES ({IDEndereco}, '{Rua}' , '{bairro}' , '{cep}' ) ")
    cn.commit()
#salvar(conexao,cursor,3,'Rua Alterosa','Progresso','890221457' )

def alterar(cn,cr,Rua,bairro,cep,IDEndereco):
    cr.execute(f"UPDATE tb_endereco SET IDEndereco={IDEndereco} , Rua='{Rua}' , bairro='{bairro}' , cep='{cep}'  WHERE IDEndereco={IDEndereco}")
    cn.commit()
# alterar(conexao,cursor,'Rua da Cooper','Glória','89022317777',2)
def deletar(cn, cr, IDEndereco):
    cr.execute(f'DELETE FROM tb_endereco WHERE IDEndereco={IDEndereco}')
    cn.commit()
deletar(conexao,cursor,3)