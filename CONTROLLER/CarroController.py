import json
from flask import *
from flask_cors import CORS
from SERVER.server import server
from SERVICE.service import ServiceCarro
from MODEL.model import Carro
from flask import current_app
import logging


logging.basicConfig(level=logging.INFO)

service = ServiceCarro()
app = server.app
CORS(app)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/carros', methods=['GET'])
def get_carr():
    logging.info('Rota da chamada: /carros')
    carros = service.find_all()
    logging.info(f'Retorno do endpoit: {carros}')
    return json.dumps(carros)

@app.route('/carros/<int:id>', methods=['GET'])
def get_id(id):
    logging.info(f'Chamada rota: /carros/{id}')
    carro = service.find_by_id(id)
    logging.info(f'Retorno: {carro}')
    return json.dumps(carro)

@app.route('/carros/insert', methods=['POST'])
def post_car():
    logging.info('Rota insert')
    json_car = request.get_json()
    logging.info(f'Dados recebidos: {json_car}')
    carro = objeto(json_car)
    service.insert_car(carro)
    return Response('Carro inserido', status=201)

@app.route('/carros/update/<int:id>', methods=['PUT'])
def put_car(id):
    logging.info('Rota update')
    json_car = request.get_json()
    logging.info(f'Dados recebidos: {json_car}')
    carro = objeto(json_car)
    service.update_car(carro, id)
    return Response('Carro atualizado', status=200)

@app.route('/carros/delete/<int:id>', methods=['DELETE'])
def delete_car(id):
    logging.info('Rota delete')
    service.delete_car(id)
    return Response('Carro deletado', status=204)



def objeto(json_response):
    logging.info('Criando obj')
    marca = json_response.get('marca')
    modelo = json_response.get('modelo')
    ano = json_response.get('ano')
    km = json_response.get('km')
    imagem = json_response.get('imagem')
    return Carro(None, modelo, marca, ano, km, imagem)