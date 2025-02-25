import logging
from DAO.FACTORY.CarroFactory import Connection
from MODEL.model import Carro
from flask import g


logging.basicConfig(level=logging.INFO)



class CarroDao:
    def __init__(self):
       pass


    def get_db(self):
        db = getattr(g, '_database', None)
        if db is None:
            connect = Connection()
            db = connect.connection_db()
            g._database = db
        return db
        
    def all_car(self):
        try:
            with self.get_db() as connect:
                logging.info('Iniciando a consulta no banco de dados.')
                cursor = connect.cursor()
                cursor.execute('''SELECT * FROM Carros''')
                lines = cursor.fetchall()
                name_coluns = [modelo[0] for modelo in cursor.description]
                list_dict = [dict(zip(name_coluns, line)) for line in lines ]
                logging.info(f'Consulta executada: {list_dict}')
                
                return list_dict
        except Exception as erro:
            logging.info(f'Falha na all_car: {erro}')
            raise erro
        
    def car_by_id(self, id):
        try:
            with self.get_db() as connect:
                logging.info('Iniciando a consulta de veiculos por ID')
                cursor = connect.cursor()
                sql = "SELECT * FROM Carros where ID= ?"
                cursor.execute(sql, (id,))
                line = cursor.fetchone()
                if line:
                    name_coluns = [modelo[0] for modelo in cursor.description]
                    car = dict(zip(name_coluns, line))
                    logging.info(f'Veiculo localizado: {car}')
                    return car
                else:
                    logging.info('Nenhum veiculo encontrado!')
        except Exception as erro:
            logging.info(f'Erro na chamada da car_by_id: {erro}')


    def insert_car(self,carro):
        try:
            with self.get_db() as connect:
                logging.info('Iniciando o processo de inserção de dados ao banco!')
                cursor = connect.cursor()
                sql = '''INSERT INTO Carros (Marca, Modelo, Ano, KM, Imagem) VALUES (?,?,?,?,?)'''
                values = (carro.marca, carro.modelo, carro.ano, carro.km, carro.imagem)
                cursor.execute(sql, values)
                car_insert = {'marca': carro.marca, 'modelo':carro.modelo, 'ano':carro.ano, 'km':carro.km, 'imagem':carro.imagem}
                connect.commit()
                logging.info(f'Dados inseridos no banco com sucesso: {car_insert}')
        except Exception as erro:
            logging.info(f'Erro na inser_car: {erro}')
            
    
    def update_car(self, carro, id):
        try:
            logging.info(f"CarroDao.update_car chamado com ID: {id}, Carro: {carro}")
            with self.get_db() as connect:
                logging.info(f'Iniciando update_car...')
                sql = '''UPDATE Carros SET Marca= ?, Modelo= ?, Ano= ?, KM= ?, Imagem = ? where id = ?'''
                cursor = connect.cursor()
                cursor.execute(sql, (carro.marca, carro.modelo, carro.ano, carro.km, carro.imagem, id))
                connect.commit()
                car_update = {'marca':carro.marca, 'modelo': carro.modelo, 'ano':carro.ano, 'km': carro.km, 'imagem':carro.imagem}
                logging.info(f'Atualizado o veiculo: {car_update}')
        except Exception as erro:
            logging.info(f'Erro na update_car: {erro}')

    def delete_car(self, id):
        try:
            with self.get_db() as connect:
                cursor = connect.cursor()
                logging.info('Iniciando delete_car....')
                sql = f'''DELETE FROM Carros where ID = {id}'''
                cursor.execute(sql)
                connect.commit()
                logging.info(f'Carro deletado com sucesso: {id}')
                return f'Carro deletado: {id}'
        except Exception as erro:
            logging.info(f'Erro ao executar a delete_car: {erro}')
            