# sales_item_inventory.py
from .database import db

sales_item_inventory = db.Table(
    'sales_item_inventory_table',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('sales_item_id', db.Integer, db.ForeignKey('sales_item_table.id')),
    db.Column('inventory_id', db.Integer, db.ForeignKey('inventory.id')),  # Update this line
    db.Column('quantity', db.Integer)
)