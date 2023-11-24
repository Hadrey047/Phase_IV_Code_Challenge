#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def Home():
        return "<h1>Restaurant Code Challenge</h1>"


@app.route('/restaurants', methods=['GET', 'POST'])
def restaurants():

    if request.method == 'GET':
        restaurants = []
        for restaurant in Restaurant.query.all():
            restaurant_dict = restaurant.to_dict()
            restaurants.append(restaurant_dict)

        response = make_response(
                restaurants,
            200
        )

        return response
    
@app.route('/restaurants/<int:id>', methods=['GET'])
def restaurants_by_id(id):
    data = request.get_json()
    
    if request.method == 'GET':
        restaurants = []
        for restaurant in Restaurant.query.filter_by(id=id).first():
            restaurant_dict = restaurant.to_dict()
            restaurants.append(restaurant_dict)

        response = make_response(
            restaurants,
            200
        )

        return response
    
    elif restaurants is None:
        return jsonify({'error': 'Restaurant not found'}), 404

   
    restaurant.name = data.get('name', restaurant.name)
    restaurant.address = data.get('address', restaurant.address)

    db.session.commit()

    return make_response(jsonify({'message': 'Restaurant updated'}), 200)


@app.route('/pizzas', methods=['GET'])
def pizzas():

    if request.method == 'GET':
        pizzas = []
        for pizza in Pizza.query.all():
            pizza_dict = pizza.to_dict()
            pizzas.append(pizza_dict)

        response = make_response(
                pizzas,
            200
        )

        return response


@app.route('/restaurant_pizzas', methods=['POST'])
def restaurant_pizzas():
    
    if request.method == 'POST':
        
        data = request.get_json()
        restaurant_pizzas = RestaurantPizza(
             price = data['price'],
             pizza_id = pizzas.id,
             restaurant_id = restaurants.id,
        )
        db.session.add(restaurant_pizzas)
        db.session.commit()
        
        response = make_response(
            restaurant_pizzas.to_dict(),
            201
        )

        return response
    
    elif restaurant_pizzas is None:
        return jsonify({'error': 'validation errors'}), 404


    
   



if __name__ == '__main__':
    app.run(port=5555)
