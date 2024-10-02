from .database import db

class Delivery(db.Model):
    __tablename__ = 'delivery_table'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    order_id = db.Column(db.String)
    vendor_name = db.Column(db.String)
    delivery_items = db.relationship('DeliveryItem', backref='delivery')