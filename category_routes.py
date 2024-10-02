from flask import Blueprint, request, jsonify
from app.models.category import Category, create_category, get_all_categories, get_category_by_id, update_category, delete_category


category_blueprint = Blueprint('category_blueprint', __name__)


# Create category
@category_blueprint.route('/categories', methods=['POST'])
def create_category_route():
    name = request.json.get('name', None)
    if name is None:
        return jsonify({"error": "Missing 'name' key"}), 400
    category = create_category(name)
    return jsonify({'id': category.id, 'name': category.name}), 201


# Get all categories
@category_blueprint.route('/categories', methods=['GET'])
def get_all_categories_route():
    categories = get_all_categories()
    return jsonify([{'id': category.id, 'name': category.name} for category in categories])


# Get category by ID
@category_blueprint.route('/categories/<id>', methods=['GET'])
def get_category_by_id_route(id):
    category = get_category_by_id(id)
    return jsonify({'id': category.id, 'name': category.name})


# Update category
@category_blueprint.route('/categories/<id>', methods=['PUT'])
def update_category_route(id):
    name = request.json.get('name', None)
    if name is None:
        return jsonify({"error": "Missing 'name' key"}), 400
    category = update_category(id, name)
    return jsonify({'id': category.id, 'name': category.name})


# Delete category
@category_blueprint.route('/categories/<id>', methods=['DELETE'])
def delete_category_route(id):
    delete_category(id)
    return jsonify({'message': 'Category deleted'}), 204