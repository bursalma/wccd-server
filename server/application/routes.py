# from flask import   Blueprint, make_response, request, jsonify

# main_bp = Blueprint('main_bp', __name__)


# @main_bp.route("/", methods=['GET'])
# def home():
#     if request.method != 'GET':
#         return make_response('Malformed request', 400)
#     my_dict = {'key': 'dictionary value'}
#     headers = {"Content-Type": "application/json"}
#     return make_response(jsonify(my_dict), 200, headers)



from flask import Blueprint, request, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User

main_bp = Blueprint('main_bp', __name__)

@main_bp.route("/", methods=['GET'])
def create_user():
    """Create a user."""
    # username = request.args.get('user')
    # email = request.args.get('email')
    username = 'bursa'
    email = 'b@g'
    if username and email:
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        if existing_user:
            return make_response(f'{username} ({email}) already created!')
        new_user = User(username=username,
                        email=email,
                        created=dt.now(),
                        bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
                        admin=False)  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes

    # return render_template('users.html',
    #                        users=User.query.all(),
    #                        title="Show Users")

    response = {'users': []}

    for each_user in User.query.all():
        response['users'].append({
            'user': each_user.username,
            'email': each_user.email
        })

    return jsonify(response)





# @main_bp.route("/users", methods=['GET'])
# def get_users():
#     users = User.query.all()

#     response = 'Here are all the users'

#     for each_user in users:
#         response += ('\n' + each_user.username)

#     return make_response(response)