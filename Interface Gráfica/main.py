import psycopg2
import psycopg2 as cn

class AppBD:
    def __init__(self):
        print('Método Construtor')

    def abrirConexão(self):
        try:
            self.connection = cn.connect(database = "postgres", user = "postgres", password = "SeIa_0O7", host = "localhost", port = "5432")
        except (Exception, psycopg2.Error) as error :
            if (self.connection):
                print('Falha ao conectar ao banco de dados', error)

    def selecionarDados (self) :
        try:
            self.abrirConexão()
            cursor = self.connection.cursor()
            print("Selecionando todos os produtos")
            cursor.execute('''select * from produto''')
            registros = cursor.fetchall()
            print(registros)

        except (Exception, psycopg2.Error) as erro :
            print("Deu Erro: ", erro)

        finally:
            if (self.connection) :
                cursor.close()
                self.connection.close()
                print("Deu certo")
        return registros

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexão()
            cursor = self.connection.cursor()
            postgres_insert_query = ''' insert into produto (codigo, nome, preco) values (%s, %s, %s)'''
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela produto")
        except (Exception, psycopg2.Error) as erro :
            if (self.connection):
                print('Falha ao inserir registro na tabela produto', erro)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("De certo, tudo inserido ")

    def atualizarDados (self, codigo, nome, preco) :
        try:
            self.abrirConexão()
            cursor = self.connection.cursor()

            print('Registro antes da atualização ')
            sql_select_query = '''select * from produto where (codigo) = %s'''
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)

            sql_update_query = '''update (produto) set (nome) = %s, (preco) = %s where (codigo) = %s '''
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, 'Registro atualizado com sucesso ')
            print("Registro depois da atualização")
            sql_select_query = '''select * from produto where codigo = %s'''
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as erro :
            print("Erro na atualização", erro)
        finally:
            if (self.connection) :
                cursor.close()
                self.connection.close()
                print("Encerrado")

    def excluirDados(self, codigo):
        try:
            self.abrirConexão()
            cursor = self.connection.cursor()
            sql_delete_query = '''Delete from produto where (codigo) = %s'''
            cursor.execute(sql_delete_query, (codigo, ))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "registro excluído com sucesso")
        except (Exception, psycopg2.Error) as erro :
            print("Deu erro de exclusão: ", erro)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("Conexão fechada")