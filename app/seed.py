from random import choice as rc

from faker import Faker

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza


fake = Faker()

with app.app_context():  
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    
    restaurants = []
    for n in range(25):
        zk = Restaurant(
            name=fake.name(), 
            address=fake.address()
        )
        restaurants.append(zk)  
    db.session.add_all(restaurants)

    
    pizzas = []
    for n in range(25):
        zk = Pizza(
            name=fake.name(), 
            ingredients=fake.text())
        pizzas.append(zk)

    db.session.add_all(pizzas)

    
    restaurant_pizzas = []
    for n in range(25):
        zk = RestaurantPizza(
            price=fake.random_int(min=5, max=20),
            pizza_id = 'pizzas.id',
            restaurants_id = 'restaurants.id'
            )
        restaurant_pizzas.append(zk)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()


