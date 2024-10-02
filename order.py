from .database import db


class Order(db.Model):
    __tablename__ = 'order_table'
    id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory_item_table.id'))
    inventory = db.relationship('InventoryItem', backref='orders')
    order_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Order('{self.id}', '{self.order_date}')"