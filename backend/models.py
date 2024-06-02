from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_vendor = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return f"<User {self.username}>"

    def save(self): 
        db.session.add(self)
        db.session.commit()
        
# PRODUCT DB
class Addproduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    image = db.Column(db.String(150), nullable=False, default='image1.jpg')
    
    def __repr__(self):
        return '<Post %r>' % self.name
    
    def save(self): 
        db.session.add(self)
        db.session.commit()




# CUSTOMER ORDERS
class CustomerOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(20), default='Pending', nullable=False)
    customer_id = db.Column(db.Integer, unique=False, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return'<CustomerOrder %r>' % self.invoice
    
    def save(self): 
        db.session.add(self)
        db.session.commit()
