from .database import db
from .sales_item_inventory import sales_item_inventory
from sqlalchemy.ext.associationproxy import association_proxy



class SalesItem(db.Model):
    __tablename__ = 'sales_item_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('category_table.id'))
    category = db.relationship('Category', backref='item_category')
    inventory_quantities = association_proxy('inventory_items', 'sales_item_inventory')
    inventory_items = db.relationship('InventoryItem', secondary='sales_item_inventory', backref='sales_items', lazy='dynamic')

    def __repr__(self):
        return f"SalesItem('{self.id}', '{self.name}')"


    def to_dict(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'name': self.name,
            'category': self.category.to_dict(),
            'inventory_items': [
                {
                    'inventory_id': item.id,
                    'quantity': assoc.quantity
                } for item, assoc in self.inventory_items
            ]
        }


    def add_inventory_item(self, inventory_id, quantity):
        from .inventory_item import InventoryItem
        """Add inventory item to sales item."""
        existing_assoc = next((assoc for assoc in self.inventory_items if assoc.id == inventory_id), None)
    
        if existing_assoc:
            # Update existing association
            existing_assoc.sales_item_inventory.quantity += quantity
        else:
            # Create new association
            new_assoc = InventoryItem.query.get(inventory_id)
            if new_assoc:
                self.inventory_items.append(new_assoc)
                db.session.add(self)
    
        db.session.commit()


    def update_inventory_quantity(self, inventory_id, quantity):
        """Update inventory quantity for a sales item."""
        existing_assoc = next((assoc for assoc in self.inventory_items if assoc.id == inventory_id), None)
        
        if existing_assoc:
            existing_assoc.quantity = quantity
            db.session.commit()


    def remove_inventory_item(self, inventory_id):
        """Remove inventory item from sales item."""
        existing_assoc = next((assoc for assoc in self.inventory_items if assoc.id == inventory_id), None)
        
        if existing_assoc:
            self.inventory_items.remove(existing_assoc)
            db.session.commit()


    def get_inventory_quantity(self, inventory_id):
        """Get inventory quantity for a sales item."""
        existing_assoc = next((assoc for assoc in self.inventory_items if assoc.id == inventory_id), None)
        
        return existing_assoc.quantity if existing_assoc else None