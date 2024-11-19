from services import userService
from flask import request, jsonify

def get():
    users = userService.get()
    return users

def login():
    customer = request.json
    user = userService.login_customer(customer['username'], customer['password'])
    if user:
        return jsonify(user), 200
    else:
        resp = {
            'status':"Error",
            'message':'User does not exist'
            }
        return jsonify(resp), 404