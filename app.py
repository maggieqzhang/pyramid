from flask import Flask, render_template, url_for, request, session, redirect, g
from flask_pymongo import PyMongo
from functools import wraps
import json
from bson import json_util
import bcrypt
import dns
import datetime
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.secret_key = 'pyramid' # super secure XD
app.config['MONGO_URI'] = 'mongodb+srv://pyramid:pyramid@openwater.chp4s.mongodb.net/pyramid?retryWrites=true&w=majority'
mongo = PyMongo(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



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

@cross_origin()         
@app.route('/', methods = ['POST', 'GET'])

def index(): #need to check if it's a restaurant or if it's a user who is trying to
    if request.method == 'POST':
        if 'type' not in session or session['type'] == 'user': #person just entered our website and wants to search w/out having logged in
            search_query = {'food': request.form['cuisine'], 'time': request.form['time']}
            return search_query

        elif session['type'] == 'restaurant':
            #find which restaurant it belongs to and then add that in their order form
            restaurants = mongo.db.restaurants
            cur_restaurant = restaurants.find_one({'address.streetAddress': session['address']})
            
            orders = mongo.db.orders
            order_id = orders.insert_one({
                    'date': "{:%B %d, %Y}".format(datetime.datetime.now()),
                    'time': request.form['time'],
                    'location': request.form['location'],
                    'maxOrders': request.form['maxOrders'],
                    'ordersFulfilled': 0,
                    'restaurant': cur_restaurant['_id'],
                    'customerOrders': {}
                    }).inserted_id
            
            cur_orders = cur_restaurant.get('orders')
            cur_orders.append(order_id)
            restaurants.update_one({'_id':cur_restaurant['_id']}, {'$set':{'orders': cur_orders}})
            return redirect(url_for('index'))
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return {1:1}

#*******************************************USER LOGIN AND REGISTER*********************************************
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return {'status': 'Already logged in' }

    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username' : request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                session['type'] = 'user'
                return { 'status' : 'Login Successful'}

        return {'status': 'Invalid username/password combination' }
    
    return { 1 : 1 }


@app.route('/register', methods=['POST', 'GET'])
def register():
    session.pop('username', None)
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert(
                    {
                    'username' : request.form['username'],
                    'password' : hashpass,
                    'email': request.form['email'],
                    'firstname' : request.form['firstname'],
                    'lastname' : request.form['lastname'],
                    'orders':[],
                    'friends': []
                    }
                    )
            session['username'] = request.form['username']
            #return redirect(url_for('index')) 
            return {'status' : 'Registration successful'}

        return {'status' : 'That username already exists!'}

    return { 1 : 1 }



@app.route('/logout',methods=['GET'])
@checkLoggedIn()
def logout():
    session.pop('username')
    return {'status':'Logout'}


#**********************Will Not be required as will be handled by react server****************************
# @app.route('/forgot',methods=['GET'])
# def forgot():
#     return redirect(url_for('index'))


# @app.route('/about')
# def about():
#     return render_template('pages/placeholder.about.html')
#*********************************Restaurant Registration and Login****************************************************************************

@app.route('/restaurantregister', methods = ['GET', 'POST'])
def restaurantRegister():
    session.pop('username', None)
    if request.method == 'POST':
        restaurants = mongo.db.restaurants
        existing_restaurant = restaurants.find_one({'address.streetAddress' : request.form['streetAddress']}) #db.restaurants.find({'address.streetAddress' : '100 chipotle'})
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

    return 'success'


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

#************************FEATURES API ENDPOINTS **************************************************************
@app.route('/addtocart', methods=['GET'])
@checkLoggedIn()
def addtocart():
    neworder=mongo.db.ordershistory.insert({
        'customer':session['username'],
        'pickuptime':request.form['pickup'],
        'bill':request.form['bill'],
        'restaurantId':request.form['restaurant'],
        'foodItem':request.form['food'],
        'status':'cart'
    })

    user=mongo.db.users.find_one({'username':session['username']})
    user['cart'].push(neworder['_id'])
    return json_util.dumps({'status':True})

@app.route('/deletefromcart/<orderid>', methods=['GET'])
@checkLoggedIn()
def deletefromcart(orderid):
    order=mongo.db.ordershistory.delete_one({'_id':orderid})
    user=mongo.db.users.find_one({'username':session['username']})
    user['cart'].pop(orderid)
    return json_util.dumps({'status':True})    


@app.route('/checkout', methods=['POST'])
@checkLoggedIn()
def checkout():
    user=mongo.db.users.find_one({'username':session['username']})
    cart=user['cart']
    orderid=cart[0]
    for i in range(len(cart)):
        order=mongo.db.ordershistory.find_one({'_id':cart[i]})
        user['orders'].push(cart[i])
        order['status']="confirmed"
        restaurant=mongo.db.restaurants.find_one({'_id':order['restaurantId']})
        restaurant['orders'].push(order['id'])
    cart=[]
    return json_util.dumps({'status':True,'orderid':orderid})



@app.route('/profile', methods=['GET'])
@checkLoggedIn()
def profile():
    user = mongo.db.users.find_one({'username' : session['username']})
    print(user['_id'])
    user.pop('_id')
    user.pop('password')
    return json_util.dumps({'user':user})


@app.route('/orderdetails/<id>', methods=['GET'])
@checkLoggedIn()
def orderdetails(id):
    if(id):
        order=mongo.db.ordershistory.find_one({'_id':id})
        print(order)
        return json_util.dumps({'success':True,'error':None,'data':order})  
    else:
        return {'error':"error"}



#takes one parameter f_username that contains username of friend to be added
@app.route('/addfriend', methods=['GET','POST'])
@checkLoggedIn()
def addFriend():
    user = mongo.db.users.find_one({'username' : session['username']})
    
    friends = user.get('friends')
    if friends is None:
        user['friends'] = []
        friends = user['friends']
    
    if 'f_username' in request.args:
        f_username = request.args['f_username']
    else:
        return {'error' : 'No Friend Username Provided. Please Specify Friend'}

    friend = mongo.db.users.find_one({'username' : f_username})

    if friend is None:
        return {'error' : 'The friend you are trying to add does not exist'}
    elif session['username'] == f_username:
        return {'error' : 'Can\'t add yourself as a friend!' }

    #Check if user and f_username are already friends
    for f in friends:
        if f == f_username:
            return {'status' : 'You are already friends!'}
    
    
    #update friends list of current user
    friends.append(f_username)
    mongo.db.users.update_one({'_id':user['_id']},{
       "$set": { 'friends': friends }
    })

    #update friends list of f_username
    user = mongo.db.users.find_one({'username' : f_username})
    friends = user.get('friends')
    if friends is None:
        user['friends'] = []
        friends = user['friends']
    friends.append(session['username'])
    mongo.db.users.update_one({'_id':user['_id']},{
       "$set": { 'friends': friends }
    })

    return { 'status' : 'Friend added successfully'}


@app.route('/listfriends', methods=['GET','POST'])
@checkLoggedIn()
def listFriends():
    user = mongo.db.users.find_one({'username' : session['username']})
    friends = user.get('friends')
    if friends is None:
        user['friends'] = []
        friends = user['friends']    
    return json_util.dumps({'friends': friends})

@app.route('/listfriends/nearby', methods = ['GET', 'POST']) #get is to display, post is to join order
@checkLoggedIn()
def nearbyFriends():
    if request.method == "GET":
        user = mongo.db.users.find_one({'username' : session['username']})
        orders = mongo.db.orders
        friends = user.get('friends')
        recent_orders = []
        if friends:
            for f in friends: #identified via friend username 
                o = f.get('orders')
                if o:
                    most_recent_order = o[-1]
                    bulk_order = orders.find_one({'_id': most_recent_order.get('parent_order')}) #need to create a checkout/card to track user orders 
                    recent_orders.append({f.get('_id'): bulk_order})
            return json_util.dumps(recent_orders)
        return "you have no friends :("
    else:
        return "you are trying to join this new order"
        

@app.route('/allrestaurants', methods=['GET'])
def allrestaurants():
    #gets list of all restaurants
    restaurants = mongo.db.restaurants.find()
    restaurant_list = []
    for r in restaurants:
        restaurant_list.append({
            'username' : r.get('username'),
            'email': r.get('email'),
            
            'address': r.get('address'),
            
            'orders':r.get('orders')
        })
    return json_util.dumps({"restaurants" : restaurant_list })


if __name__ == '__main__':
    app.run(debug=True)
