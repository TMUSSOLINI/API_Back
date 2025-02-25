from DAO.CarroDAO import CarroDao
import logging


logging.basicConfig(level=logging.INFO)

class ServiceCarro:
    def __init__(self):
        self.carro = CarroDao()


    def find_all(self):
        logging.info('Buscando find_all')
        return self.carro.all_car()
    

    def find_by_id(self, id):
        logging.info('Buscando by id')
        return self.carro.car_by_id(id)
    

    def delete_car(self, id):
        logging.info('Delete car')
        return self.carro.delete_car(id)
    

    def update_car(self, carro, id):
        logging.info('Update')
        return self.carro.update_car(carro, id)
    

    def insert_car(self, carro):
        logging.info('insert')
        return self.carro.insert_car(carro)