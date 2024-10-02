from flask import Blueprint, request, jsonify
from app.models.vendor import Vendor, create_vendor, get_all_vendors, get_vendor_by_id, update_vendor, delete_vendor


vendor_blueprint = Blueprint('vendor_blueprint', __name__)


# Create vendor
@vendor_blueprint.route('/vendors', methods=['POST'])
def create_vendor_route():
    name = request.json['name']
    contact = request.json['contact']
    vendor = create_vendor(name, contact)
    return jsonify({'id': vendor.id, 'name': vendor.name, 'contact': vendor.contact}), 201


# Get all vendors
@vendor_blueprint.route('/vendors', methods=['GET'])
def get_all_vendors_route():
    vendors = get_all_vendors()
    return jsonify([{'id': vendor.id, 'name': vendor.name, 'contact': vendor.contact} for vendor in vendors])


# Get vendor by ID
@vendor_blueprint.route('/vendors/<id>', methods=['GET'])
def get_vendor_by_id_route(id):
    vendor = get_vendor_by_id(id)
    return jsonify({'id': vendor.id, 'name': vendor.name, 'contact': vendor.contact})


# Update vendor
@vendor_blueprint.route('/vendors/<id>', methods=['PUT'])
def update_vendor_route(id):
    name = request.json['name']
    contact = request.json['contact']
    vendor = update_vendor(id, name, contact)
    return jsonify({'id': vendor.id, 'name': vendor.name, 'contact': vendor.contact})


# Delete vendor
@vendor_blueprint.route('/vendors/<id>', methods=['DELETE'])
def delete_vendor_route(id):
    delete_vendor(id)
    return jsonify({'message': 'Vendor deleted'}), 204