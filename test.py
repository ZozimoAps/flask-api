import unittest
from settings import environment
from app.models import db
from app import create_app


class Test(unittest.TestCase):

    # Este metodo nos permite realizar un proceso antes de que se
    # ejecuten nuestras pruebas
    def setUp(self):
        self.app = create_app(environment['test'])
        self.client = self.app.test_client()

        self.content_type = 'application/json'

        with self.app.app_context():
            db.create_all()

    # Cuando nuestras pruebas se terminen podremos ejecutar otro proceso en
    # con este metodo
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def get_all_data(self):
        response = self.client.get('http://127.0.0.1:5000/api/v1/tasks')
        self.assertEqual(200, response.status_code)
        self.assertIn('No hay entradas', response.data)


if __name__ == '__main__':
    unittest.main()
