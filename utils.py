from app.models.database import db
from flask import jsonify

def update_model_instance(model_instance, data, schema):
    """Update a model instance with the provided data"""
    errors = schema.validate(data)
    if errors:
        return jsonify({'errors': errors}), 400
    
    for key, value in data.items():
        setattr(model_instance, key, value)
    
    db.session.commit()
    return jsonify(schema.dump(model_instance))