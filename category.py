from .database import db


class Category(db.Model):
    __tablename__ = 'category_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    sales_items = db.relationship('SalesItem', backref='category')

    def __repr__(self):
        return f"Category('{self.id}', '{self.name}')"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sales_items': [item.to_dict() for item in self.sales_items]
        }


# Create
def create_category(name):
    """Create a new category."""
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return category


# Get all
def get_all_categories():
    """Get all categories."""
    return Category.query.all()


# Get by ID
def get_category_by_id(id):
    """Get category by ID."""
    return Category.query.get(id)


# Update
def update_category(id, name):
    """Update category name."""
    category = get_category_by_id(id)
    if category:
        category.name = name
        db.session.commit()
    return category


# Delete
def delete_category(id):
    """Delete category."""
    category = get_category_by_id(id)
    if category:
        db.session.delete(category)
        db.session.commit()


# Get category sales items
def get_category_sales_items(id):
    """Get sales items for a category."""
    category = get_category_by_id(id)
    if category:
        return category.sales_items
    return []