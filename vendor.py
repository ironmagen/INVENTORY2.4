from .database import db
from .inventory_item import InventoryItem


class Vendor(db.Model):
    __tablename__ = 'vendor_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact_name = db.Column(db.String(255), nullable=False)
    contact_email = db.Column(db.String(255), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    inventory_items = db.relationship('InventoryItem', backref='vendor')

    def __repr__(self):
        return f"Vendor('{self.id}', '{self.name}')"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact_name': self.contact_name,
            'contact_email': self.contact_email,
            'contact_phone': self.contact_phone,
            'address': self.address,
            'inventory_items': [
                {
                    'inventory_item_id': item.id,
                    'item_name': item.item_name
                } for item in self.inventory_items
            ]
        }


# Create
def create_vendor(name, contact_name, contact_email, contact_phone, address):
    vendor = Vendor(
        name=name,
        contact_name=contact_name,
        contact_email=contact_email,
        contact_phone=contact_phone,
        address=address
    )
    db.session.add(vendor)
    db.session.commit()
    return vendor


# Get all
def get_all_vendors():
    return Vendor.query.all()


# Get by ID
def get_vendor_by_id(id):
    return Vendor.query.get(id)


# Update
def update_vendor(id, name, contact_name, contact_email, contact_phone, address):
    vendor = get_vendor_by_id(id)
    if vendor:
        vendor.name = name
        vendor.contact_name = contact_name
        vendor.contact_email = contact_email
        vendor.contact_phone = contact_phone
        vendor.address = address
        db.session.commit()
    return vendor


# Delete
def delete_vendor(id):
    vendor = get_vendor_by_id(id)
    if vendor:
        db.session.delete(vendor)
        db.session.commit()