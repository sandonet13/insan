from app import app
from app.controller import UserController, ProfileController, CampaignController
from flask import request, jsonify
import simplekv.memory
from app import api
from flask_restx import Api, Resource, reqparse



@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()

# @app.route('/user/<id>')
# def usersDetail(id):
#     print(id)
#     return UserController.show(id)

# @app.route('/profile/<user_id>')
# def profileDetail(user_id):
#     print(user_id)
#     return ProfileController.show(user_id)

# @app.route('/profile/')
# def profile():
#     return ProfileController.index()

# @app.route('/campaign/')
# def campaigns():
#     return CampaignController.index()

# @app.route('/campaign/<user_id>')
# def campaignDetail(user_id):
#     print(user_id)
#     return CampaignController.show(user_id)

@app.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)

@app.route('/login', methods=['POST'])
def login():
    return UserController.login()

@app.route('/campaign', methods=['POST', 'GET'])
def campaign():
    if request.method == 'GET':
        return CampaignController.index()
    else:
        return CampaignController.store()


@app.route('/campaign/<id>', methods=['PUT', 'GET', 'DELETE'])
def campaignDetail(id):
    if request.method == 'GET':
        return CampaignController.show(id)
    elif request.method == 'PUT':
        return CampaignController.update(id)
    elif request.method == 'DELETE':
        return CampaignController.delete(id)

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if request.method == 'GET':
        return ProfileController.index()
    else:
        return ProfileController.store()


@app.route('/profile/<id>', methods=['PUT', 'GET', 'DELETE'])
def profileDetail(id):
    if request.method == 'GET':
        return ProfileController.show(id)
    elif request.method == 'PUT':
        return ProfileController.update(id)
    elif request.method == 'DELETE':
        return ProfileController.delete(id)

@api.route('/logout')
class HelloWorldParameter(Resource):
    def get(self):
        return UserController.sign_out()

# @app.route("/logout")
# def signout():
#     return UserController.sign_out()

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return 'hello'
