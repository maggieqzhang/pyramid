from flask import Flask, render_template, url_for, request, session, redirect, g
from flask_pymongo import PyMongo
import bcrypt
import dns

app = Flask(__name__)


app.config['MONGO_URI'] = 'mongodb+srv://pyramid:<password>@openwater.chp4s.mongodb.net/<dbname>?retryWrites=true&w=majority'

mongo = PyMongo(app)
print(mongo)

@app.before_request
def before_request():
    if "username" in session:
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})
        g.login_user = login_user

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == "POST":
        #search for cuisine types inside the restaurant database 
        
    else:
        if 'username' in session:
            return 'You are logged in as ' + g.login_user['username']
    return {'DONE':'HEllo'}

@app.route('/login', methods=['POST'])
def login():
    
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        print(existing_user)

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

@app.route('/profile')
def profile():
    pass 
    

if __name__ == '__main__':
    app.secret_key = 'pyramid'
    app.run(debug=True)
