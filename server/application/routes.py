from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from datetime import datetime
from .models import db, Race

main_bp = Blueprint('main_bp', __name__)

class Convict(MethodView):

    def get(self, id):
        return f"Responding to a GET request: {id}"

    def post(self):
        return f"Responding to a POST request:"

    def delete(self, id):
        return f"Responding to a delete request: {id}"

main_bp.add_url_rule(
    "/api/convict/<id>", 
    view_func=Convict.as_view("convict"))


class View(MethodView):

    def get(self, message):
        return f"Responding to a GET request: {message}"

    def post(self, message):
        return f"Responding to a POST request: {message}"

    def put(self, message):
        return f"Responding to a put request: {message}"

    def patch(self, message):
        return f"Responding to a patch request: {message}"

    def delete(self, message):
        return f"Responding to a delete request: {message}"

main_bp.add_url_rule(
    "/api/view/<message>", 
    view_func=View.as_view("view"))



# @main_bp.route("/", methods=['GET'])
# def create_user():

#     headers = {"Content-Type": "application/json"}

#     if request.method != 'GET':
#         return make_response(jsonify({'message': 'malformed request'}), 400, headers)

#     # username = request.args.get('user')
#     # email = request.args.get('email')

#     username = 'bursa'
#     email = 'b@g'

#     if username and email:
#         existing_user = User.query.filter(User.username == username or User.email == email).first()

#         if existing_user:
#             exists_response = {'message': f'{username} ({email}) already exists'}

#             return make_response(jsonify(exists_response), 200, headers)

#         new_user = User(username=username,
#                         email=email,
#                         created=datetime.now(),
#                         admin=False)

#         db.session.add(new_user)
#         db.session.commit()

#     response = {'users': []}

#     for each_user in User.query.all():
#         response['users'].append({
#             'user': each_user.username,
#             'email': each_user.email
#         })


#     return make_response(jsonify(response), 200, headers)


# @main_bp.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404



# @main_bp.route("/users", methods=['GET'])
# def get_users():
#     users = User.query.all()

#     response = 'Here are all the users'

#     for each_user in users:
#         response += ('\n' + each_user.username)

#     return make_response(response)