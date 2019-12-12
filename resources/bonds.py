import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

bond = Blueprint('bonds', 'bond')

# Index Route
@bond.route('/', methods=["GET"])
def get_all_bonds():
    print('bond index route connected')
    try: 
        bonds = [model_to_dict(bond)
            for bond in models.bond.select()]
        print(bonds)
        return jsonify(data=bonds, status={"code": 200, "message": "bonds is connected"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "error getting the resources"})

# New Route
@bond.route('/', methods=["POST"])
def create_bonds():
    payload = request.get_json()
    print(payload, 'New bond accepted')

    bond = models.bond.create(**payload)

    print(dir(bond))

    bond_dict = model_to_dict(bond)
    return jsonify(data=bond_dict, status={"code": 201, "message": "New bond card is added to the indexs"})

# Show Route
@bond.route('/<id>', methods=["GET"])
def get_one_bond(id):
    print(id)

    bond = models.bond.get_by_id(id)

    return jsonify(data={"bond": model_to_dict(bond)}, status={"code": 200, "message": "bond Show is showing"})

# Update Route
@bond.route('/<id>', methods=['PUT'])
def update_bond(id):
    print('we are hitting here')
    payload = request.get_json()
    query = models.bond.update(**payload).where(models.bond.id == id)
    query.execute()
    bond = models.bond.get_by_id(id)
    bond_dict = model_to_dict(bond)
    return jsonify(data=bond_dict, status={"code": 200, "message": "bond is updated!"})

# Delete Route
@bond.route('/<id>', methods=["DELETE"])
def delete_bond(id):
    query = models.bond.delete().where(models.bond.id == id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "bond has been successfully deleted"})