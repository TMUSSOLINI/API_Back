from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def connection_db():
    conn = sqlite3.connect('Cars.db')
    return conn

def create_db():
    connect = connection_db()
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE Carros(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   Marca text not null,
                    Modelo text not null,
                     Ano text not null,
                      KM real not null,
                       Imagem text not null)''')
    connect.commit()
    connect.close()

def list_car():
    connect = connection_db()
    cursor = connect.cursor()
    cursor.execute('''SELECT * FROM Carros''')
    lines = cursor.fetchall()
    name_coluns = [modelo[0] for modelo in cursor.description]
    list_dict = [dict(zip(name_coluns, line)) for line in lines ]
    connect.close()
    return list_dict

def insert_car(marca, modelo, ano, km, imagem):
    connect = connection_db()
    cursor = connect.cursor()
    sql = '''INSERT INTO Carros (Marca, Modelo, Ano, KM, Imagem) VALUES (?,?,?,?,?)'''
    values = (marca, modelo, ano, km, imagem)
    cursor.execute(sql, values)
    connect.commit()
    connect.close()

def car(id):
    connect = connection_db()
    cursor = connect.cursor()
    sql = "SELECT * FROM Carros where ID= ?"
    cursor.execute(sql, (id,))
    line = cursor.fetchone()
    if line:
        name_coluns = [modelo[0] for modelo in cursor.description]
        car = dict(zip(name_coluns, line))
        connect.close()
        return car
    else:
        connect.close()
        return jsonify({'Message': 'Não foi encontrado!'})
    

if __name__ == '__main__':

    @app.route('/')
    def home():
        return jsonify({'Message':'Estou funcionando!'})
    

    @app.route('/teste')
    def insert():
        insert_car('Fiat','Palio', '2021',100.15, 'google')
        return jsonify({'Message': 'Inseri os dados no banco!'})

    @app.route('/todos')
    def all():
        lista_de = list_car()
        return jsonify(lista_de)
    
    @app.route('/unico/<int:id>')
    def unico(id):
        carro = car(id)
        return carro

    app.run(debug=True)