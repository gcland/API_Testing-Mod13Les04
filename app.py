from flask import Flask
from database import db
from schema import ma
from limiter import limiter
from sqlalchemy.orm import Session

from models.customer import Customer
from models.user import User
from models.employee import Employee
from models.order import Order
from models.product import Product
from models.orderProduct import order_product
from models.production import Production
from models.role import Role
from models.customerManagementRole import CustomerManagementRole

from routes.customerBP import customer_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint
from routes.employeeBP import employee_blueprint
from routes.productionBP import production_blueprint
from routes.userBP import user_blueprint

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)

    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    app.register_blueprint(production_blueprint, url_prefix='/productions')
    app.register_blueprint(user_blueprint, url_prefix='/users')

def configure_rate_limit():
    limiter.limit("5000 per day")(customer_blueprint)
    limiter.limit("5000 per day")(product_blueprint)
    limiter.limit("5000 per day")(order_blueprint)
    limiter.limit("5000 per day")(employee_blueprint)
    limiter.limit("5000 per day")(product_blueprint)

def init_roles_customers_info_data():       # add sample customers and users (customerAccounts) 
    with Session(db.engine) as session:
        with session.begin():
            customers = [
                Customer(name = "Customer_A", email = 'customerA@gmail.com', phone = "123-123-1234"),
                Customer(name = "Customer_G", email = 'customerG@yahoo.com', phone = "456-456-3429"),
                Customer(name = "Customer_Z", email = 'customerZ@outlook.com', phone = "986-567-3452")
            ]

            users = [
                User(username = "csA", password = 'passwordA', customer_id=1),
                User(username = "csB", password = 'passwordB', customer_id=2),
                User(username = "csC", password = 'passwordC', customer_id=3)  
            ]
            session.add_all(customers)
            session.add_all(users)

def init_roles_data():
    with Session(db.engine) as session:
        with session.begin():
            roles = [
                Role(role_name='admin'),
                Role(role_name='user'),
                Role(role_name='guest')
            ]
            session.add_all(roles)

def init_roles_customers_data():
    with Session(db.engine) as session:
        with session.begin():
            roles_customer = [
                CustomerManagementRole(customer_management_id = 1, role_id=1),
                CustomerManagementRole(customer_management_id = 1, role_id=2),
                CustomerManagementRole(customer_management_id = 1, role_id=3)
            ]
            session.add_all(roles_customer)


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blue_print_config(app)
    configure_rate_limit()
    
    with app.app_context():
        db.drop_all()
        db.create_all()
        init_roles_customers_info_data()
        init_roles_data()
        init_roles_customers_data()

    app.run(debug=True)