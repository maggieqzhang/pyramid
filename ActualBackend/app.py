from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from functools import wraps
import json
from bson import json_util
import bcrypt

app = Flask(__name__)
app.secret_key = 'pyramid'
app.config['MONGO_URI'] = 'mongodb+srv://pyramid:pyramid@openwater.chp4s.mongodb.net/pyramid?retryWrites=true&w=majority'
mongo = PyMongo(app)


def checkLoggedIn():
    def check(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(session['username'])
            print(session)
            if 'username' in session:
                return func(*args, **kwargs)
            else:
                return {"Error":"Please Login"}
        return inner
    return check               




@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return {'Hi':'Hi'}

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})
        print(existing_user)

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username' : request.form['username'], 'password' : hashpass, 'orders':[]})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

@app.route('/profile', methods=['GET'])
@checkLoggedIn()
def profile():
    user = mongo.db.users.find_one({'username' : session['username']})
    user.pop('_id')
    user.pop('password')
    return json_util.dumps({'user':user})


@app.route('/transactiondetails/<id>', methods=['GET'])
@checkLoggedIn()
def txdetails(id):
    if(id):
        # tx=mongo.db.transactions.find_one({'_id':id})
        # print(tx)
        return {'success':id}  
    else:
        return {'error':"error"}    

  






if __name__ == '__main__':
    app.run(debug=True)