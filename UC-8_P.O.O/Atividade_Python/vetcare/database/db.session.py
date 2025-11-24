import mysql.connector
from mysql.connector import Error

class DB:
    def __init__(self, host='localhost', user='root', password='1234', database='vetcare'):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor(dictionary=True)  # retorna dict
            return True
        except Error as e:
            print(f"Erro ao conectar: {e}")
            return False

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()

    def create_tutor(self, tutor):
        try:
            self.connect()

            query = """
                INSERT INTO tutores (nome, telefone)
                VALUES (%s, %s)
            """
            values = (tutor.nome, tutor.telefone)

            self.cursor.execute(query, values)
            self.conn.commit()

            print("Tutor cadastrado com sucesso!")
        except Error as e:
            print("Erro ao cadastrar tutor:", e)
        finally:
            self.close()


    def get_tutores(self):
        try:
            self.connect()

            self.cursor.execute("SELECT * FROM tutores")
            return self.cursor.fetchall()

        except Error as e:
            print("Erro ao buscar tutores:", e)
            return []
        finally:
            self.close()

    def update_tutor(self, tutor_id, novo_nome, novo_telefone):
        try:
            self.connect()

            query = """
                UPDATE tutores
                SET nome=%s, telefone=%s
                WHERE id=%s
            """
            values = (novo_nome, novo_telefone, tutor_id)

            self.cursor.execute(query, values)
            self.conn.commit()

            print("Tutor atualizado!")
        except Error as e:
            print("Erro ao atualizar tutor:", e)
        finally:
            self.close()

    def delete_tutor(self, tutor_id):
        try:
            self.connect()

            query = "DELETE FROM tutores WHERE id=%s"
            self.cursor.execute(query, (tutor_id,))
            self.conn.commit()

            print("Tutor removido!")
        except Error as e:
            print("Erro ao deletar tutor:", e)
        finally:
            self.close()
