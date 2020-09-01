from flask import Flask, render_template, url_for, request, session, redirect, g
from flask_pymongo import PyMongo
from functools import wraps
import json
from bson import json_util
import bcrypt
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            session['type'] = 'user' 
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

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


@app.route('/profile', methods=['GET'])
@checkLoggedIn()
def profile():
    user = mongo.db.users.find_one({'username' : session['username']})
    user.pop('_id')
    user.pop('password')
    return json_util.dumps({'user':user})


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
