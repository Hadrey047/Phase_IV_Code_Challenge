from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(100))
    
    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas', back_populates='restaurants')

    def __repr__(self):
        return f'<Restaurant {self.name} and {self.address}>'

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurants')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    ingredients = db.Column(db.String())
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizzas', back_populates='pizzas')

     
    def __repr__(self):
        return f'<Pizza {self.name} and {self.ingredients}>'
    
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    
    # serialize_rules = ('-restaurant.restaurantpizzas','-pizza.restaurantpizzas',)

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float())
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restuarant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
   
    def __repr__(self):
       return f'RestaurantPizza {self.price}'
    
# add any models you may need. 