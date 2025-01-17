import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

stock = Blueprint('stocks', 'stock')

# Index Route
@stock.route('/', methods=["GET"])
def get_all_stocks():
    print('stock index route connected')
    try: 
        stocks = [model_to_dict(stock)
            for stock in models.Stock.select()]
        print(stocks)
        return jsonify(data=stocks, status={"code": 200, "message": "Stocks is connected"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "error getting the resources"})

# New Route
@stock.route('/', methods=["POST"])
def create_stocks():
    payload = request.get_json()
    print(payload, 'New stock accepted')

    stock = models.Stock.create(**payload)

    print(dir(stock))

    stock_dict = model_to_dict(stock)
    return jsonify(data=stock_dict, status={"code": 201, "message": "New stock card is added to the indexs"})

# Show Route
@stock.route('/<id>', methods=["GET"])
def get_one_stock(id):
    print(id)

    stock = models.Stock.get_by_id(id)

    return jsonify(data={"stock": model_to_dict(stock)}, status={"code": 200, "message": "Stock Show is showing"})

# Update Route
@stock.route('/<id>', methods=['PUT'])
def update_stock(id):
    print('we are hitting here')
    payload = request.get_json()
    query = models.Stock.update(**payload).where(models.Stock.id == id)
    query.execute()
    stock = models.Stock.get_by_id(id)
    stock_dict = model_to_dict(stock)
    return jsonify(data=stock_dict, status={"code": 200, "message": "stock is updated!"})

# Delete Route
@stock.route('/<id>', methods=["DELETE"])
def delete_stock(id):
    query = models.Stock.delete().where(models.Stock.id == id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "stock has been successfully deleted"})

