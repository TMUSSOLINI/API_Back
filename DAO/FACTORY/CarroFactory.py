import sqlite3
import logging


DATABASE = '/mnt/wwn-0x50014ee21161f38b-part1/Trabalho/Automacao/POC/Cars.db'

class Connection:

    def create_db():
        with sqlite3.connect(DATABASE) as connect:
            logging.info('Conectado ao banco, iniciando processo de criação da tabela: Carros.')
            cursor = connect.cursor()
            cursor.execute('''CREATE TABLE Carros(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Marca text not null,
                            Modelo text not null,
                            Ano text not null,
                            KM real not null,
                            Imagem text not null)''')
            logging.info('Criado a tabela Carros!')
            connect.commit()


    def connection_db(self):
        try:
            conn = sqlite3.connect(DATABASE)
            logging.info('Iniciando a conexão ao banco de dados...')
            logging.info('Conectado ao banco: %s', DATABASE)
            return conn
        except sqlite3.Error as e:
            logging.error(f'Erro ao conectar ao banco de dados: {e}')
            raise