from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from functools import wraps
import json
from bson import json_util
import bcrypt
import forms

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
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('pages/status.html', status="You are logged in as "+session['username'])

    return render_template('pages/home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = forms.LoginForm(request.form)

    if 'username' in session:
        return render_template('pages/status.html', status="You are already logged in")

    if request.method == 'POST' and form.validate():
        users = mongo.db.users
        login_user = users.find_one({'username' : request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('profile'))

        return render_template('pages/status.html', status="Invalid username or password")
    
    return render_template('forms/login.html',form=form)


@app.route('/logout',methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template('pages/status.html', status="You have logged out")
    return render_template('pages/status.html', status="You are not logged in")


@app.route('/forgot',methods=['GET'])
def forgot():
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = forms.RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        
        users = mongo.db.users
        
        existing_user = users.find_one({'username' : request.form['name']})
        print(existing_user)
        
        if existing_user is None:
            
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username' : request.form['name'], 'password' : hashpass, 'orders':[],
             'email':request.form['email'], 'firstname':request.form['first'],'lastname':request.form['last']})
            session['username'] = request.form['name']
            return redirect(url_for('index'))
        
        return render_template('pages/status.html', status="That username already exists.")

    return render_template('forms/register.html',form=form)

@app.route('/profile', methods=['GET'])
@checkLoggedIn()
def profile():
    user = mongo.db.users.find_one({'username' : session['username']})

    return render_template('pages/status.html', status="Welcome " + user['firstname'] + "!")
    
    #user.pop('_id')
    #user.pop('password')
    #return json_util.dumps({'user':user})
    



if __name__ == '__main__':
    app.run(debug=True)