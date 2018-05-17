#!/usr/bin/env python

from flask import (Flask, render_template, request, redirect, jsonify, url_for,
                   flash)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from models import Base, Arrangement, Flower, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

engine = create_engine('sqlite:///floralArrangements.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = json.loads(
    open('client_secret.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Floral Arrangements Web Client"

app = Flask(__name__)


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data

    try:
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('User is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ''' " style = "width: 300px; height: 300px;border-radius: 150px;
    -webkit-border-radius: 150px;-moz-border-radius: 150px;"> '''
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('''Failed to revoke token for
        given user.''', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showCatalog'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showCatalog'))


@app.route('/')
@app.route('/arrangements', methods=['GET'])
def showCatalog():
    arrangements = session.query(Arrangement).all()
    if 'username' not in login_session:
        return render_template('publicArrangements.html',
                               arrangements=arrangements)
    return render_template('arrangements.html', arrangements=arrangements)


@app.route('/arrangements/new', methods=['GET', 'POST'])
def createArrangement():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newArrangement = Arrangement(name=request.form['name'],
                                     description=request.form['description'],
                                     base_price=request.form['base_price'],
                                     user_id=login_session['user_id'])
        session.add(newArrangement)
        flash('New Arrangement %s Successfully Created' % newArrangement.name)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template('newArrangement.html')


@app.route('/arrangements/<int:arrangement_id>/edit', methods=['GET', 'POST'])
def editArrangement(arrangement_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedArrangement = session.query(
        Arrangement).filter_by(id=arrangement_id).one()
    if editedArrangement.user_id != login_session['user_id']:
        return '''<script>function myFunction() {alert('You are not authorized
         to edit this arrangement. Please create your own arrangement in order
          to edit.');}</script><body onload='myFunction()'>'''
    if request.method == 'POST':
        if request.form['name']:
            editedArrangement.name = request.form['name']
        if request.form['description']:
            editedArrangement.description = request.form['description']
        if request.form['base_price']:
            editedArrangement.base_price = request.form['base_price']
        session.add(editedArrangement)
        session.commit()
        flash('Arrangement Successfully Edited %s' % editedArrangement.name)
        return redirect(url_for('showCatalog'))
    else:
        return render_template('editArrangement.html',
                               arrangement=editedArrangement)


@app.route('/arrangements/<int:arrangement_id>/delete',
           methods=['GET', 'POST'])
def deleteArrangement(arrangement_id):
    if 'username' not in login_session:
        return redirect('/login')
    arrangementToDelete = session.query(
        Arrangement).filter_by(id=arrangement_id).one()
    if arrangementToDelete.user_id != login_session['user_id']:
        return '''<script>function myFunction() {alert('You are not authorized
         to delete this arrangement. Please create your own arrangement in
          order to delete.');}</script><body onload='myFunction()'>'''
    if request.method == 'POST':
        session.delete(arrangementToDelete)
        flash('%s Successfully Deleted' % arrangementToDelete.name)
        session.commit()
        return redirect(url_for('showCatalog', arrangement_id=arrangement_id))
    else:
        return render_template('deleteArrangement.html',
                               arrangement=arrangementToDelete)


@app.route('/arrangements/<int:arrangement_id>', methods=['GET'])
def showArrangement(arrangement_id):
    arrangement = session.query(Arrangement).filter_by(id=arrangement_id).one()
    creator = getUserInfo(arrangement.user_id)
    flowers = session.query(Flower).filter_by(
        arrangement_id=arrangement_id).all()
    if ('username' not in login_session or
        creator.id != login_session['user_id']):
            return render_template('publicFlowers.html', flowers=flowers,
                                   arrangement=arrangement, creator=creator)
    else:
        return render_template('flowers.html', flowers=flowers,
                               arrangement=arrangement, creator=creator)


@app.route('/arrangements/<int:arrangement_id>/new', methods=['GET', 'POST'])
def addFlower(arrangement_id):
    if 'username' not in login_session:
        return redirect('/login')
    arrangement = session.query(Arrangement).filter_by(id=arrangement_id).one()
    if login_session['user_id'] != arrangement.user_id:
        return '''<script>function myFunction() {alert('You are not authorized
         to add menu items to this arrangement. Please create your own
          arrangement in order to add items.');}</script>
          <body onload='myFunction()'>'''
    if request.method == 'POST':
        newFlower = Flower(name=request.form['name'],
                           description=request.form['description'],
                           price=request.form['price'],
                           arrangement_id=arrangement_id,
                           user_id=arrangement.user_id)
        session.add(newFlower)
        session.commit()
        flash('New Flower %s Successfully Added!' % (newFlower.name))
        return redirect(url_for('showArrangement',
                                arrangement_id=arrangement_id))
    else:
        return render_template('newFlower.html', arrangement=arrangement)


@app.route('/arrangements/<int:arrangement_id>/<int:flower_id>',
           methods=['GET', 'POST'])
def editFlower(arrangement_id, flower_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedFlower = session.query(Flower).filter_by(id=flower_id).one()
    arrangement = session.query(Arrangement).filter_by(id=arrangement_id).one()
    if login_session['user_id'] != arrangement.user_id:
        return '''<script>function myFunction() {alert('You are not authorized
         to edit menu items to this arrangement. Please create your own
          arrangement in order to edit items.');}</script>
          <body onload='myFunction()'>'''
    if request.method == 'POST':
        if request.form['name']:
            editedFlower.name = request.form['name']
        if request.form['description']:
            editedFlower.description = request.form['description']
        if request.form['price']:
            editedFlower.price = request.form['price']
        session.add(editedFlower)
        session.commit()
        flash('Flower Successfully Edited')
        return redirect(url_for('showFlowers', arrangement_id=arrangement_id))
    else:
        return render_template('editFlower.html',
                               arrangement_id=arrangement_id,
                               flower_id=flower_id, flower=editedFlower)


@app.route('/arrangements/<int:arrangement_id>/<int:flower_id>/delete',
           methods=['GET', 'POST'])
def deleteFlower(arrangement_id, flower_id):
    if 'username' not in login_session:
        return redirect('/login')
    arrangement = session.query(Arrangement).filter_by(id=arrangement_id).one()
    flowerToDelete = session.query(Flower).filter_by(id=flower_id).one()
    if login_session['user_id'] != arrangement.user_id:
        return '''<script>function myFunction() {alert('You are not authorized
         to delete flowers in this arrangement. Please create your own
          arrangement in order to delete items.');}</script>
          <body onload='myFunction()'>'''
    if request.method == 'POST':
        session.delete(flowerToDelete)
        session.commit()
        flash('Flower Successfully Deleted!')
        return redirect(url_for('showArrangement',
                                arrangement_id=arrangement_id))
    else:
        return render_template('deleteFlower.html', flower=flowerToDelete)


@app.route('/users/JSON/')
def userJSON():
    try:
        users = session.query(User).all()
        return jsonify(User=[i.serialize for i in users])
    except:
        return "No users in the database"


@app.route('/arrangements/JSON/')
def arrangementsJSON():
    try:
        arrangements = session.query(Arrangement).all()
        return jsonify(Arrangment=[i.serialize for i in arrangements])
    except:
        return "No arrangements in the database"


@app.route('/arrangements/<int:arrangement_id>/JSON/')
def arrangmentFlowersJSON(arrangement_id):
    try:
        flowers = session.query(Flower).filter_by(
                                    arrangement_id=arrangement_id).all()
        return jsonify(Flower=[i.serialize for i in flowers])
    except:
        return "No flowers in the arrangement"


@app.route('/arrangements/<int:arrangement_id>/<int:flower_id>/JSON/')
def flowerJSON(arrangement_id, flower_id):
    try:
        flower = session.query(Flower).filter_by(id=flower_id).one()
        return jsonify(Flower=flower.serialize)
    except:
        return "Flower not in the database"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
