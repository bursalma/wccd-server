from flask import Blueprint, request, make_response, jsonify
from datetime import datetime
from .models import db, User

main_bp = Blueprint('main_bp', __name__)

@main_bp.route("/", methods=['GET'])
def create_user():

    headers = {"Content-Type": "application/json"}

    if request.method != 'GET':
        return make_response(jsonify({'message': 'malformed request'}), 400, headers)

    # username = request.args.get('user')
    # email = request.args.get('email')

    username = 'bursa'
    email = 'b@g'

    if username and email:
        existing_user = User.query.filter(User.username == username or User.email == email).first()

        if existing_user:
            exists_response = {'message': f'{username} ({email}) already exists'}

            return make_response(jsonify(exists_response), 200, headers)

        new_user = User(username=username,
                        email=email,
                        created=datetime.now(),
                        admin=False)

        db.session.add(new_user)
        db.session.commit()

    response = {'users': []}

    for each_user in User.query.all():
        response['users'].append({
            'user': each_user.username,
            'email': each_user.email
        })

    return make_response(jsonify(response), 200, headers)





# @main_bp.route("/users", methods=['GET'])
# def get_users():
#     users = User.query.all()

#     response = 'Here are all the users'

#     for each_user in users:
#         response += ('\n' + each_user.username)

#     return make_response(response)