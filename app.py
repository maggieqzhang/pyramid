from flask import Flask, render_template, url_for, request, session, redirect, g
from flask_pymongo import PyMongo
from functools import wraps
import json
from bson import json_util
import bcrypt
import forms
import dns
from datetime import date
from forms import *


app = Flask(__name__)
app.secret_key = 'pyramid' # super secure XD
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

'''
@app.before_request
def before_request():
    if "username" in session:
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})
        g.login_user = login_user
'''
@app.route('/', methods = ['POST', 'GET'])
def index(): #need to check if it's a restaurant or if it's a user who is trying to buy 
    if request.method == 'POST':
        if 'type' not in session or session['type'] == 'user': #person just entered our website and wants to search w/out having logged in
            search_query = {'food': request.form['cuisine'], 'time': request.form['time'] }
            #[URGENT]figure out how to pass this over to the next search query step
            
            
        elif session['type'] == 'restaurant': 
            #find which restaurant it belongs to and then add that in their order form 
            restaurants = mongo.db.restaurants
            restaurantName = restaurants.update(
                    {'address.streetAddress': session['address'] }, {$addToSet:{'orders': {
                    'date': date.today(),
                    'time': request.form['time'],
                    'maxOrders': request.form['maxOrders'],
                    'ordersFulfilled': 0 
                    }}}
                )
            return redirect(url_for('index'))
    if 'username' in session: 
        return 'You are logged in as ' + session['username']

    return {1:1} 

'''
    if 'username' in session:
        return render_template('pages/status.html', status="You are logged in as "+session['username'])
    #return render_template('pages/home.html')
    return render_template('forms/search.html', form = form)
'''



@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    form = forms.LoginForm(request.form)

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            session['type'] = 'user' 
            return redirect(url_for('index'))
    '''
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
    session.pop('username', None)
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert(
                    {
                    'username' : request.form['username'], 
                    'password' : hashpass, 
                    'email': request.form['email'], 
                    'orders':[]
                    }
                    )
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'That username already exists!'
    return render_template('forms/register.html')


'''
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
'''
@app.route('/profile', methods=['GET'])
@checkLoggedIn()
def profile():
    user = mongo.db.users.find_one({'username' : session['username']})
    return render_template('pages/status.html', status="Welcome " + user['firstname'] + "!")
    
    #user.pop('_id')
    #user.pop('password')
    #return json_util.dumps({'user':user})
    



@app.route('/restaurantregister', methods = ['GET', 'POST'])
def restaurantRegister():
    session.pop('username', None)
    if request.method == 'POST':
        restaurants = mongo.db.restaurants
        existing_restaurant = restaurants.find_one({'restaurant' : request.form['restaurant']})
        if existing_restaurant is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            restaurants.insert(
                    {
                    'username' : request.form['username'], 
                    'password' : hashpass, 
                    'email': request.form['email'], 
                    'address':{
                    'restaurant': request.form['restaurant'], 
                    'streetAddress': request.form['streetAddress'],
                    'city': request.form['city'],
                    'state': request.form['state'],
                    'zipcode': request.form['zipcode']},
                    'orders':[]
                     }
                    )
            session['username'] = request.form['restaurant']
            session['type'] = 'restaurant'
            session['address'] = request.form['streetAddress']
            return redirect(url_for('index'))
        
        return 'We already have your restaurant in our system!'
    
    return render_template('forms/register.html')

    
@app.route('/restaurantlogin', methods = ['GET', 'POST'])
def restaurantLogin():
    restaurants = mongo.db.restaurants
    login_user = restaurants.find_one({'username' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            session['type'] = 'restaurant' 
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


if __name__ == '__main__':
    app.run(debug=True)
