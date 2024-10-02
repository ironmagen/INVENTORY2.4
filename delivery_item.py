from .database import db

class DeliveryItem(db.Model):
    __tablename__ = 'delivery_item_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery_table.id'))
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory_table.id'))
    quantity = db.Column(db.Integer)
    delivery = db.relationship('Delivery', backref='delivery_items')
    inventory_item = db.relationship('Inventory', backref='inventory_delivery_items')