from flask import Blueprint, make_response, request, jsonify

# Set up a Blueprint
main_bp = Blueprint('main_bp', __name__)


@main_bp.route("/", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    my_dict = {'key': 'dictionary value'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(my_dict), 200, headers)