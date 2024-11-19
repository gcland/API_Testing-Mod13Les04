import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services import customerService
from models.customer import Customer
from models.schemas.customerSchema import customer_schema
from controllers import customerController

class TestCustomerEndpoints(unittest.TestCase):

    @patch('controllers.customerController.load')
    def test_save_customer(self, mock_customer):

        faker = Faker()
        mock_user = MagicMock()
        mock_user.name = faker.name()
        mock_user.id = 8
        mock_user.email = faker.email()
        mock_user.phone = faker.phone_number()
        test_input = {
            'id': mock_user.id,
            "name": mock_user.name,
            "email": mock_user.email,
            "phone": mock_user.phone

        }
        print(test_input)
        mock_customer.return_value.load.return_value = test_input
        response = customerController.save()
        print(response)
        # self.assertEqual(customerController.save(test_input), test_input)


if __name__ == "__main__":
    unittest.main()
