import MySQLdb

#Listando Todos dados da tabela
def listar_todos(c):
    c.execute('SELECT * FROM tb_endereco')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)

#Buscar pelo id
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM tb_endereco WHERE ID = {id}')
    endereco = c.fetchone()
    print(endereco)
buscar_por_id(c,1)
#Buscar por cep
# def buscar_por_cep(c,cep):
#     c.execute(f"SELECT * FROM tb_endereco WHERE CEP like '%{cep}%' ")
#     for e  in  c.fetchall():
#         print(e)


#Salvar Pessoa
# def salvar(cn,cr,Rua,bairro,cep,IDEndereco='NULL'):
#     if IDEndereco == None:
#         IDEndereco = 'NULL'
#     cr.execute(f"INSERT INTO tb_endereco (IDEndereco,Rua,bairro,cep,IDEndereco) VALUES ('{IDEndereco}', '{Rua}' , {cep} , {bairro} ) ")
#     cn.commit()

# #Alterar Pessoa
# def alterar(cn,cr,Id_pessoa,Nome,SobreNome,Idade, endereco_id='NULL'):
#     cr.execute(f"UPDATE tb_pessoa SET Nome='{Nome}', Sobrenome='{SobreNome}' , Idade={Idade} , endereco_id={endereco_id}  WHERE Id_pessoa={Id_pessoa}")
#     cn.commit()

# #Deletar Pessoa
# def deletar(cn, cr, Id_pessoa):
#     cr.execute(f'DELETE FROM tb_pessoa WHERE Id_pessoa={Id_pessoa}')
#     cn.commit()

# conexao = MySQLdb.connect(host='localhost', database='aula_bd2', user='root', passwd='')
# cursor= conexao.cursor()

# #Comandos Para CRUD ;

# # listar_todos(cursor)
# # buscar_por_id(cursor, 2)
# # buscar_por_sobrenome(cursor,'Sil')
# # salvar(conexao,cursor,'Pablo','Cardoso',12,2)
# # alterar(conexao,cursor, 3 ,'Rafaela','Mendes',18, 1)
# # deletar(conexao,cursor,3)