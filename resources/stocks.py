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

# Show Route
@stock.route('/<id>', methods=["GET"])
def get_one_stock(id):
    print(id)

    # stock = models.Stock.get_by_id(id)

    return jsonify(data={"stock": 200, "message": "Stock Show is showing"})

