from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from users_ap import users_resource
from data.db_session import global_init

app = Flask(__name__)
api = Api(app)
# для списка объектов
api.add_resource(users_resource.UsersListResource, '/api/v2/users')

# для одного объекта
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
global_init("db/book_store.db")


if __name__ == '__main__':
    app.run()
