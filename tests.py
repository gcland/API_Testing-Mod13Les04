import unittest
from unittest.mock import MagicMock, patch
from flask import Flask
from faker import Faker
from werkzeug.security import generate_password_hash
from services import customerService
from models.customer import Customer
from models.schemas.customerSchema import customer_schema
from controllers.customerController import save

class TestCustomerEndpoints(unittest.TestCase):
# customer_data = customer_schema.load(test_input)
    @patch('models.schemas.customerSchema.customer_schema.load')
    @patch('services.customerService.save')
    def test_save_customer(self, mock_load, mock_save):
        app = Flask(__name__)
        app.config['TESTING'] = True
        faker = Faker()
        mock_user = MagicMock()
        mock_user.name = faker.name()
        # mock_user.id = 8
        mock_user.email = faker.email()
        mock_user.phone = faker.phone_number()
        test_input = {
            # 'id': mock_user.id,
            "name": mock_user.name,
            "email": mock_user.email,
            "phone": mock_user.phone

        }
        mock_load.return_value = test_input
        mock_save.return_value = test_input

        with app.test_request_context(json = test_input):
            response, status_code = save()

        mock_load.assert_called_once_with(test_input)
        mock_save.assert_called_once_with(test_input)

        print(response, status_code)
        
        self.assertEqual(status_code, 201)
        self.assertIn("name", response.json)


if __name__ == "__main__":
    unittest.main()
