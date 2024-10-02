from .database import db
from sqlalchemy import Enum
from .sales_item import SalesItem as SalesItem
from .sales_item_inventory import sales_item_inventory as sales_item_inventory


class InventoryItem(db.Model):
    __tablename__ = 'inventory_item_table'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category_table.id'))
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor_table.id'))
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    units = db.Column(db.String(50), nullable=False)
    status = db.Column(Enum('In Stock', 'Low Stock', 'Out of Stock', name='status_enum'), nullable=False)
    par = db.Column(db.Integer, nullable=False)
    order_strike = db.Column(db.Integer, nullable=False)
    cost_on_hand = db.Column(db.DECIMAL(10, 2), nullable=False)
    category = db.relationship('Category', backref='inventory_items')
    vendor = db.relationship('Vendor', backref='vendor_inventory')
    sales_items = db.relationship('SalesItem', secondary=sales_item_inventory, backref='inventory_items')

    def __repr__(self):
        return f"InventoryItem('{self.id}', '{self.item_name}')"

    def to_dict(self):
        return {
            'id': self.id,
            'item_name': self.item_name,
            'category_id': self.category_id,
            'vendor_id': self.vendor_id,
            'price': self.price,
            'stock': self.stock,
            'units': self.units,
            'status': self.status,
            'par': self.par,
            'order_strike': self.order_strike,
            'cost_on_hand': self.cost_on_hand,
            'sales_items': [
                {
                    'sales_item_id': item.id,
                    'quantity': next(
                        (assoc.quantity for assoc in sales_item_inventory.query.filter(
                            sales_item_inventory.c.sales_item_id == item.id,
                            sales_item_inventory.c.inventory_id == self.id
                        )), None)
                } for item in self.sales_items
            ]
        }


# Create
def create_inventory(item_name, category_id, vendor_id, price, stock, units, status, par, order_strike, cost_on_hand):
    inventory = InventoryItem(
        item_name=item_name,
        category_id=category_id,
        vendor_id=vendor_id,
        price=price,
        stock=stock,
        units=units,
        status=status,
        par=par,
        order_strike=order_strike,
        cost_on_hand=cost_on_hand
    )
    db.session.add(inventory)
    db.session.commit()
    return inventory


# Get all
def get_all_inventories():
    return InventoryItem.query.all()


# Get by ID
def get_inventory_by_id(id):
    return InventoryItem.query.get(id)


# Update
def update_inventory(id, item_name, category_id, vendor_id, price, stock, units, status, par, order_strike, cost_on_hand):
    inventory = get_inventory_by_id(id)
    if inventory:
        inventory.item_name = item_name
        inventory.category_id = category_id
        inventory.vendor_id = vendor_id
        inventory.price = price
        inventory.stock = stock
        inventory.units = units
        inventory.status = status
        inventory.par = par
        inventory.order_strike = order_strike
        inventory.cost_on_hand = cost_on_hand
        db.session.commit()
    return inventory


# Delete
def delete_inventory(id):
    inventory = get_inventory_by_id(id)
    if inventory:
        db.session.delete(inventory)
        db.session.commit()


# Get inventory sales items
def get_inventory_sales_items(id):
    inventory = get_inventory_by_id(id)
    if inventory:
        return inventory.sales_items
    return []


# Update inventory quantity
def update_inventory_quantity(id, quantity):
    inventory = get_inventory_by_id(id)
    if inventory:
        inventory.stock = quantity
        db.session.commit()
    return inventory


# Get used quantity
def get_used_quantity(id):
    inventory = get_inventory_by_id(id)
    if inventory:
        used_quantity = sales_item_inventory.query.filter_by(
            inventory_id=inventory.id).with_entities(
            db.func.sum(sales_item_inventory.c.quantity)).scalar() or 0
        return used_quantity
    return 0


# Get available quantity
def get_available_quantity(id):
    inventory = get_inventory_by_id(id)
    if inventory:
        return inventory.stock - get_used_quantity(id)
    return 0