from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


def create_db():
    conn = sqlite3.connect('Cars.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE Carros(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   Marca text not null,
                    Modelo text not null,
                     Ano text not null,
                      KM real not null,
                       Imagem text not null)''')
    conn.commit()
    conn.close()

    print('Criado')

@app.route('/')
def home():
    return jsonify({'Message':'Estou funcionando!'})

if __name__ == '__main__':
    app.run(debug=True)