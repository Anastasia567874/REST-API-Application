from flask_restful import abort, Resource
from data.db_session import create_session, global_init
from jobs_ap.jobs import Jobs
from flask import jsonify
from jobs_ap.reqparse import parser


def abort_if_user_not_found(job_id):
    session = create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_user_not_found(job_id)
        session = create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'jobs': job.to_dict(
            only=('team_leader', 'job', 'work_size', 'start_date', 'end_date', 'is_finished'))})

    def delete(self, job_id):
        abort_if_user_not_found(job_id)
        session = create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('team_leader', 'job', 'work_size', 'start_date', 'end_date', 'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})