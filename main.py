from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO, filename='Logging.log', format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)
CORS(app)

DATABASE = 'Cars.db'

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
        


def connection_db():
    try:
        conn = sqlite3.connect(DATABASE)
        logging.info('Iniciando a conexão ao banco de dados...')
        return conn
    except sqlite3.Error as e:
        logging.error(f'Erro ao conectar ao banco de dados: {e}')
        raise


def list_car():
    with connection_db() as connect:
        logging.info('Iniciando a consulta no banco de dados, retornando todos os veiculos cadastrados!')
        cursor = connect.cursor()
        cursor.execute('''SELECT * FROM Carros''')
        lines = cursor.fetchall()
        name_coluns = [modelo[0] for modelo in cursor.description]
        list_dict = [dict(zip(name_coluns, line)) for line in lines ]
        logging.info('Consulta executada!')
        
        return list_dict


def insert_car(marca, modelo, ano, km, imagem):
    with connection_db() as connect:
        logging.info('Iniciando o processo de inserção de dados ao banco!')
        cursor = connect.cursor()
        sql = '''INSERT INTO Carros (Marca, Modelo, Ano, KM, Imagem) VALUES (?,?,?,?,?)'''
        values = (marca, modelo, ano, km, imagem)
        cursor.execute(sql, values)
        connect.commit()
        logging.info('Dados inseridos no banco com sucesso!')
        


def car(id):
    with connection_db() as connect:
        logging.info('Iniciando a consulta de veiculos por ID...')
        cursor = connect.cursor()
        sql = "SELECT * FROM Carros where ID= ?"
        cursor.execute(sql, (id,))
        line = cursor.fetchone()
        if line:
            name_coluns = [modelo[0] for modelo in cursor.description]
            car = dict(zip(name_coluns, line))
            logging.info('Veiculo localizado!')
            
            return car
        else:
            logging.info('Nenhum veiculo encontrado!')
            
            return jsonify({'Message': 'Não foi encontrado!'})
    

if __name__ == '__main__':

    @app.route('/')
    def home():
        return jsonify({'Message':'Estou funcionando!'})
    

    @app.route('/teste')
    def insert():
        insert_car('Fiat','Palio', '2021',100.15, 'google')
        return jsonify({'Message': 'Inseri os dados no banco!'})

    @app.route('/allcar')
    def all():
        list_cars = list_car()
        if list_cars:
            return jsonify(list_cars), 200
        else:
            return jsonify({'Message': 'Não existem veiculos carregados!'}), 404
    
    @app.route('/car/<int:id>')
    def unico(id):
        carro = car(id)
        if carro:
            return jsonify(carro), 200
        else:
            return jsonify({'Message': 'Id não encontrado!'}), 404

    app.run(debug=True)