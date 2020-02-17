from flask import Flask, make_response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .admin import admin_routes
from .specialist import specialist_routes
from .viewer import viewer_routes
import sqlite3

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.DevConfig')
app.register_blueprint(admin_routes.admin_bp)
app.register_blueprint(specialist_routes.specialist_bp)
app.register_blueprint(viewer_routes.viewer_bp)

db = SQLAlchemy(app)


@app.route("/", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    my_dict = {'key': 'dictionary value'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(my_dict), 200, headers)


# class User(db.Model):
#     """Model for user accounts."""

#     __tablename__ = 'users'
#     id = db.Column(db.Integer,
#                    primary_key=True)
#     username = db.Column(db.String(64),
#                          index=False,
#                          unique=True,
#                          nullable=False)
#     email = db.Column(db.String(80),
#                       index=True,
#                       unique=True,
#                       nullable=False)
#     created = db.Column(db.DateTime,
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     bio = db.Column(db.Text,
#                     index=False,
#                     unique=False,
#                     nullable=True)
#     admin = db.Column(db.Boolean,
#                       index=False,
#                       unique=False,
#                       nullable=False)

#     def __repr__(self):
#         return '<User {}>'.format(self.username)


# from datetime import datetime as dt

# @app.route('/user', methods=['GET'])
# def create_user():
#     """Create a user."""
#     # username = request.args.get('user')
#     # email = request.args.get('email')
#     username = 'mali'
#     email = 'mali@g.com'
#     if username and email:
#         new_user = User(username=username,
#                         email=email,
#                         created=dt.now(),
#                         bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
#                         admin=False)  # Create an instance of the User class
#         db.session.add(new_user)  # Adds new User record to database
#         db.session.commit()  # Commits all changes
#     return make_response(f"{new_user} successfully created!")

# db.create_all()






# app.config['SQLALCHEMY_DATABASE_URI'] = ''





# class user_test(db.Model):
#     """Model for user accounts."""

#     __tablename__ = 'user_test'
#     user_id = db.Column(db.Integer,
#                         primary_key=True)
#     username = db.Column(db.String(45),
#                          index=False,
#                          unique=True,
#                          nullable=False)
#     password = db.Column(db.String(200),
#                          index=False,
#                          unique=True,
#                          nullable=False)
#     full_name = db.Column(db.String(200),
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     email = db.Column(db.String(80),
#                       index=True,
#                       unique=True,
#                       nullable=False)                

#     def __repr__(self):
#         return '<User {}>'.format(self.username)




# from flask import   Flask, request, url_for, abort, \
#                     session, redirect, flash
# from werkzeug.utils import secure_filename
# from markupsafe import escape



# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/' + secure_filename(f.filename))

# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404


# return jsonify({})

# @app.route("/me")
# def me_api():
#     user = get_current_user()
#     return {
#         "username": user.username,
#         "theme": user.theme,
#         "image": url_for("user_image", filename=user.image),
#     }

# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return jsonify([user.to_json() for user in users])

# # _______________ session ______________
# # Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'N\xf2}#\xf0\xbb\x8f5MH\xde\xa6-\x04@k'

# @app.route('/')
# def index():
#     if 'username' in session:
#         return 'Logged in as %s' % escape(session['username'])
#     return 'You are not logged in'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))
#     # _______________ session ______________

# app.logger.debug('A value for debugging')
# app.logger.warning('A warning occurred (%d apples)', 42)
# app.logger.error('An error occurred')

# pip install flask-sqlalchemy

# if __name__ == '__main__':
#     app.run(host='127.0.0.1',port=8000,debug=True)



# from socket import gethostname
# [...]

# if __name__ == '__main__':
#     db.create_all()
#     if 'liveconsole' not in gethostname():
#         app.run()