#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show all restaurants
@app.route('/')
@app.route('/restaurants')
def restaurantsShow():
    return "Show All Restaurants"

# Create new restaurant
@app.route('/restaurants/new')
def restaurantNew():
    return "New Restaurant"

# Edit existing restaurant
@app.route('/restaurants/<int:restaurant_id>/edit')
def restaurantEdit(restaurant_id):
    return "Edit Restaurant"

# Delete existing restaurant
@app.route('/restaurants/<int:restaurant_id>/delete')
def restaurantDelete(restaurant_id):
    return "Delete Restaurant"

# Show restaurant menu
@app.route('/restaurants/<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):
    return "Show All MenuItems"

# Create new menu item
@app.route('/restaurants/<int:restaurant_id>/menu/new')
def restaurantNewMenuItem(restaurant_id):
    return "Create new Menu Item"

# Edit existing menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def restaurantEditMenuItem(restaurant_id, menu_id):
    return "Edit menu item"

# Delete Menu Item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def restaurantDeleteMenuItem(restaurant_id, menu_id):
    return "Delete menu item"

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
