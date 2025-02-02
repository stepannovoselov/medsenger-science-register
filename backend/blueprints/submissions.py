from flask import Blueprint, request
from backend.methods import *

submission_blueprint = Blueprint('submissions', __name__)


@submission_blueprint.route('/project/<int:project_id>/patients/<int:patient_id>/submissions', methods=['get'])
@creates_response
@requires_user
def get_submissions(user, project_id, patient_id):
    project = find_project_by_id_for_user(user, project_id)
    patient = find_patient_by_id(patient_id)

    submissions = get_patient_submissions(project, patient)

    return as_dict(submissions)


@submission_blueprint.route('/project/<int:project_id>/patients/<int:patient_id>/submissions', methods=['post'])
@creates_response
@requires_user
def add_submission(user, project_id, patient_id):
    data = request.json

    form_id = data.get('form_id')
    answers = data.get('answers')

    project = find_project_by_id_for_user(user, project_id)
    patient = find_patient_by_id(patient_id)
    form = find_form_by_id(form_id)

    submission = submit_form(user, patient, form, answers)

    return submission.as_dict()
