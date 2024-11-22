import unittest
from unittest.mock import MagicMock, patch
from flask import Flask
from faker import Faker
from controllers import customerController 
from controllers import employeeController 
from controllers import orderController 
from controllers import productController 
from controllers import productionController 
from datetime import date

class TestCustomerEndpoints(unittest.TestCase):
    @patch('models.schemas.customerSchema.customer_schema.load')
    @patch('services.customerService.save')
    def test_save_customer(self, mock_load, mock_save):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_user = MagicMock()
        mock_user.name = faker.name()
        mock_user.email = faker.email()
        mock_user.phone = faker.phone_number()
        test_input = {
            "name": mock_user.name,
            "email": mock_user.email,
            "phone": mock_user.phone

        }
        mock_load.return_value = test_input
        mock_save.return_value = test_input

        with app.test_request_context(json = test_input):
            response, status_code = customerController.save()

        mock_load.assert_called_once_with(test_input)
        mock_save.assert_called_once_with(test_input)

        print(response, status_code)
        
        self.assertEqual(status_code, 201)
        self.assertIn("name", response.json)
    
    @patch('services.customerService.get')
    def test_get_customer(self, mock_get):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_user = MagicMock()
        mock_user.name = faker.name()
        mock_user.email = faker.email()
        mock_user.phone = faker.phone_number()
        test_input = {
            "name": mock_user.name,
            "email": mock_user.email,
            "phone": mock_user.phone

        }
        mock_get.return_value = test_input

        with app.test_request_context():
            response, status_code = customerController.get()

        print(response, status_code)
        
        self.assertEqual(status_code, 200)


class TestProductEndpoints(unittest.TestCase):
    @patch('models.schemas.productSchema.product_schema.load')
    @patch('services.productService.save')
    def test_save_product(self, mock_load, mock_save):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_product = MagicMock()
        mock_product.name = faker.name()
        mock_product.price = faker.random_number()
        test_input = {
            "name": mock_product.name,
            "price": mock_product.price

        }
        mock_load.return_value = test_input
        mock_save.return_value = test_input

        with app.test_request_context(json = test_input):
            response, status_code = productController.save()

        mock_load.assert_called_once_with(test_input)
        mock_save.assert_called_once_with(test_input)

        print(response, status_code)
        
        self.assertEqual(status_code, 201)
        self.assertIn("name", response.json)
    
    @patch('services.productService.get')
    def test_get_product(self, mock_get):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_product = MagicMock()
        mock_product.name = faker.name()
        mock_product.price = faker.random_number()
        test_input = {
            "name": mock_product.name,
            "price": mock_product.price

        }
        mock_get.return_value = test_input

        with app.test_request_context():
            response, status_code = productController.get()

        print(response, status_code)
        
        self.assertEqual(status_code, 200)

class TestOrderEndpoints(unittest.TestCase):
    @patch('models.schemas.orderSchema.order_schema.load')
    @patch('services.orderService.save')
    def test_save_order(self, mock_load, mock_save):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_order = MagicMock()
        mock_order.customer_id = faker.random_number()
        mock_order.date = date.today().isoformat()
        mock_order.products = [{"id": 1}, {"id": 2}, {"id": 5}]
        test_input = {
            "customer_id": mock_order.customer_id,
            "date": mock_order.date,
            "products": mock_order.products
        }

        mock_load.return_value = test_input
        mock_save.return_value = test_input

        with app.test_request_context(json = test_input):
            response, status_code = orderController.save()

        mock_load.assert_called_once_with(test_input)
        mock_save.assert_called_once_with(test_input)

        print(response, status_code)
        
        self.assertEqual(status_code, 201)
        self.assertIn("customer_id", response.json)
    
    @patch('services.orderService.get')
    def test_get_order(self, mock_get):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_order = MagicMock()
        mock_order.customer_id = faker.random_number()
        mock_order.date = faker.date()
        mock_order.products = [{"id": 1}, {"id": 2}, {"id": 5}]
        test_input = {
            "customer_id": mock_order.customer_id,
            "date": mock_order.date,
            "products": mock_order.products
        }

        mock_get.return_value = test_input

        with app.test_request_context():
            response, status_code = orderController.get()

        print(response, status_code)
        
        self.assertEqual(status_code, 200)

class TestProductionEndpoints(unittest.TestCase):
    @patch('models.schemas.productionSchema.production_schema.load')
    @patch('services.productionService.save')
    def test_save_production(self, mock_load, mock_save):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_production = MagicMock()
        mock_production.product_id = faker.random_number()
        mock_production.employee_id = faker.random_number()
        mock_production.quantity_produced = faker.random_number()
        mock_production.date_produced = faker.date()
        test_input = {
            "product_id": mock_production.product_id,
            "employee_id": mock_production.employee_id,
            "quantity_produced": mock_production.quantity_produced,
            "date_produced": mock_production.date_produced
        }
        mock_load.return_value = test_input
        mock_save.return_value = test_input

        with app.test_request_context(json = test_input):
            response, status_code = productionController.save()

        mock_load.assert_called_once_with(test_input)
        mock_save.assert_called_once_with(test_input)

        print(response, status_code)
        
        self.assertEqual(status_code, 201)
        self.assertIn("product_id", response.json)
    
    @patch('services.productionService.get')
    def test_get_production(self, mock_get):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_production = MagicMock()
        mock_production.product_id = faker.random_number()
        mock_production.employee_id = faker.random_number()
        mock_production.quantity_produced = faker.random_number()
        mock_production.date_produced = date.today().isoformat()
        test_input = {
            "product_id": mock_production.product_id,
            "employee_id": mock_production.employee_id,
            "quantity_produced": mock_production.quantity_produced,
            "date_produced": mock_production.date_produced
        }
        mock_get.return_value = test_input

        with app.test_request_context():
            response, status_code = productionController.get()

        print(response, status_code)
        
        self.assertEqual(status_code, 200)

class TestEmployeeEndpoints(unittest.TestCase):
    @patch('models.schemas.employeeSchema.employee_schema.load')
    @patch('services.employeeService.save')
    def test_save_employee(self, mock_load, mock_save):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_employee = MagicMock()
        mock_employee.name = faker.name()
        mock_employee.position = "employee_title"
        test_input = {
            "name": mock_employee.name,
            "position": mock_employee.position,

        }
        mock_load.return_value = test_input
        mock_save.return_value = test_input

        with app.test_request_context(json = test_input):
            response, status_code = employeeController.save()

        mock_load.assert_called_once_with(test_input)
        mock_save.assert_called_once_with(test_input)

        print(response, status_code)
        
        self.assertEqual(status_code, 201)
        self.assertIn("name", response.json)
    
    @patch('services.employeeService.get')
    def test_get_employee(self, mock_get):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_employee = MagicMock()
        mock_employee.name = faker.name()
        mock_employee.position = "employee_title"
        test_input = {
            "name": mock_employee.name,
            "position": mock_employee.position,

        }
        mock_get.return_value = test_input

        with app.test_request_context():
            response, status_code = employeeController.get()

        print(response, status_code)
        
        self.assertEqual(status_code, 200)

if __name__ == "__main__":
    unittest.main()
