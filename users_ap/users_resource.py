from flask_restful import abort, Resource
from data.db_session import create_session, global_init
from users_ap.users import User
from flask import jsonify
from users_ap.reqparse import parser
from werkzeug.security import generate_password_hash
import os

#os.chdir('..')
#global_init("db/book_store.db")


def abort_if_user_not_found(user_id):
    session = create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)
        return jsonify({'users': user.to_dict(
            only=('name', 'surname', 'age', 'email', 'hashed_password'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('name', 'surname', 'age', 'email', 'hashed_password')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            email=args['email'],
            hashed_password=generate_password_hash(args['hashed_password'])
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})