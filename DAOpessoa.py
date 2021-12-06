from conexão import Conexao
from pessoa import Pessoa


class DAOPessoa:
    def __init__(self):

        print("in init")

    def adicionar_pessoa(self):

        nome = input('Nome:')
        cpf = input('cpf: ')
        endereco = input('Endereço: ')
        bairro = input('Bairro: ')
        cep = input('CEP: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')

        cadastrar_funcionario_empresa = input('Deseja vincular esse funcionario a empresa?')
        if cadastrar_funcionario_empresa.upper() == "S":

            id_empresa = input('Digite o id da empresa ')
            novaPessoa = Pessoa(nome, endereco, bairro, cep, cidade, estado, id_empresa)
        else:
            id_empresa = 0
            novaPessoa = Pessoa(nome, endereco, bairro, cep, cidade, estado, id_empresa)

        # Adiciona Banco isso aqui tudo eu não sei:
        con = Conexao.getConnection('Estabelecendo Conexao')
        cursor = con.cursor()
        query = "INSERT INTO pessoa(nome, endereco, bairro, cep, cidade, estado, id_empresa) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        dados = novaPessoa.nome, novaPessoa.endereco, novaPessoa.bairro, novaPessoa.cep, novaPessoa.cidade, novaPessoa.estado,novaPessoa.id_empresa
        cursor.execute(query, dados)
        con.commit()

    def lista_pessoas(self):
            try:
                con = Conexao.getConnection('Estabelecendo Conexao')
                cursor = con.cursor()
                query = "select * from pessoa"
                cursor.execute(query)
                # get all records
                records = cursor.fetchall()

                print("\n Mostra dados")
                for row in records:
                    print("Id = ", row[0], )
                    print("Nome = ", row[1])
                    print("Endereco  = ", row[3])
                    print("Bairro = ", row[4], )
                    print("Cep = ", row[5])
                    print("Cidade  = ", row[6])
                    print("Estado = ", row[7])

            except TypeError as error:
                print("Failed to delete record from table: {}".format(error))

            finally:
                cursor.close()
                con.close()
                print("MySQL connection is closed")

    def deletaPessoa(self):
            try:
                con = Conexao.getConnection('Estalecendo Conexao')
                cursor = con.cursor()
                nomePessoa = input('Nome da pessoa:')
                query = "DELETE from pessoa WHERE nome = %s"
                cursor.execute(query, nomePessoa)
                con.commit()
            except TypeError as error:
                print("Failed to delete record from table: {}".format(error))

            finally:
                cursor.close()
                con.close()
                print("MySQL connection is closed")
