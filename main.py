from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from users_ap import users_resource
from jobs_ap import jobs_resource
from data.db_session import global_init

app = Flask(__name__)
api = Api(app)
api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:job_id>')
global_init("db/book_store.db")


if __name__ == '__main__':
    app.run()
