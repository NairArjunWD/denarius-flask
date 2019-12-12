import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

etf = Blueprint('etfs', 'etf')

# Index Route
@etf.route('/', methods=["GET"])
def get_all_etfs():
    print('etf index route connected')
    try: 
        etfs = [model_to_dict(etf)
            for etf in models.etf.select()]
        print(etfs)
        return jsonify(data=etfs, status={"code": 200, "message": "etfs is connected"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "error getting the resources"})

# New Route
@etf.route('/', methods=["POST"])
def create_etfs():
    payload = request.get_json()
    print(payload, 'New etf accepted')

    etf = models.etf.create(**payload)

    print(dir(etf))

    etf_dict = model_to_dict(etf)
    return jsonify(data=etf_dict, status={"code": 201, "message": "New etf card is added to the indexs"})

# Show Route
@etf.route('/<id>', methods=["GET"])
def get_one_etf(id):
    print(id)

    etf = models.etf.get_by_id(id)

    return jsonify(data={"etf": model_to_dict(etf)}, status={"code": 200, "message": "etf Show is showing"})

# Update Route
@etf.route('/<id>', methods=['PUT'])
def update_etf(id):
    print('we are hitting here')
    payload = request.get_json()
    query = models.etf.update(**payload).where(models.etf.id == id)
    query.execute()
    etf = models.etf.get_by_id(id)
    etf_dict = model_to_dict(etf)
    return jsonify(data=etf_dict, status={"code": 200, "message": "etf is updated!"})

# Delete Route
@etf.route('/<id>', methods=["DELETE"])
def delete_etf(id):
    query = models.etf.delete().where(models.etf.id == id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "etf has been successfully deleted"})

