from flask import Blueprint, jsonify, request
from app.models.inventory_item import InventoryItem
from app.schemas.inventory_schema import InventorySchema
from app.models.database import db
from app.utils.utils import update_model_instance


inventory_blueprint = Blueprint('inventory_blueprint', __name__)


@inventory_blueprint.route('/inventory', methods=['GET'])
def get_all_inventory():
    inventory = InventoryItem.query.all()
    schema = InventorySchema(many=True)
    return jsonify(schema.dump(inventory))


@inventory_blueprint.route('/inventory/<int:id>', methods=['GET'])
def get_inventory(id):
    inventory = InventoryItem.query.get(id)
    schema = InventorySchema()
    return jsonify(schema.dump(inventory))


@inventory_blueprint.route('/inventory', methods=['POST'])
def create_inventory():
    data = request.get_json()
    schema = InventorySchema()
    errors = schema.validate(data)
    if errors:
        return jsonify({'errors': errors}), 400
    inventory = InventoryItem(**data)
    db.session.add(inventory)
    db.session.commit()
    return jsonify(schema.dump(inventory)), 201


@inventory_blueprint.route('/inventory/<int:id>', methods=['PUT'])
def update_inventory(id):
    inventory = InventoryItem.query.get(id)
    data = request.get_json()
    schema = InventorySchema()
    return update_model_instance(inventory, data, schema)


@inventory_blueprint.route('/inventory/<int:id>', methods=['DELETE'])
def delete_inventory(id):
    inventory = InventoryItem.query.get(id)
    db.session.delete(inventory)
    db.session.commit()
    return jsonify({'message': 'Inventory deleted successfully'}), 200