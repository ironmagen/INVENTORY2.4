from flask import Blueprint, jsonify, request
from app.models.order import Order
from app.schemas.order_schema import OrderSchema
from app.models.database import db
from app.utils.utils import update_model_instance


order_blueprint = Blueprint('order_blueprint', __name__)


# Define routes with consistent naming and docstrings
@order_blueprint.route('/orders', methods=['GET'])
def get_all_orders() -> dict:
    """
    Retrieves all orders.
    
    Returns:
        dict: JSON response with all orders.
    """
    orders = Order.query.all()
    schema = OrderSchema(many=True)
    return jsonify(schema.dump(orders))


@order_blueprint.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id: int) -> dict:
    """
    Retrieves an order by ID.
    
    Args:
        order_id (int): Order ID.
    
    Returns:
        dict: JSON response with the order.
    """
    order = Order.query.get(order_id)
    schema = OrderSchema()
    return jsonify(schema.dump(order))


@order_blueprint.route('/orders', methods=['POST'])
def create_order() -> dict:
    """
    Creates a new order.
    
    Returns:
        dict: JSON response with the created order.
    """
    data = request.get_json()
    schema = OrderSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify({'errors': errors}), 400
    order = Order(**data)
    db.session.add(order)
    db.session.commit()
    return jsonify(schema.dump(order)), 201


@order_blueprint.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id: int) -> dict:
    """
    Updates an existing order.
    
    Args:
        order_id (int): Order ID.
    
    Returns:
        dict: JSON response with the updated order.
    """
    order = Order.query.get(order_id)
    data = request.get_json()
    schema = OrderSchema()
    return update_model_instance(order, data, schema)


@order_blueprint.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id: int) -> dict:
    """
    Deletes an order by ID.
    
    Args:
        order_id (int): Order ID.
    
    Returns:
        dict: JSON response with deletion message.
    """
    order = Order.query.get(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200