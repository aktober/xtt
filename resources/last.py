from flask import jsonify
from flask_restful import Resource, reqparse
from operations import models


class LastResource(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('currency', location='args', type=str)
        parser.add_argument('number', location='args', type=int)

        args = parser.parse_args(strict=True)
        currency = args['currency']
        number = args['number']

        last_ops = []
        query = models.Operations.query.order_by(-models.Operations.requested_time)

        if currency:
            query = query.filter_by(currency=currency)

        if number:
            query = query.limit(number)
            last_ops = models.operations_schema.dump(query)
        else:
            query = query.first()
            el = models.operation_schema.dump(query)
            last_ops.append(el)

        return jsonify({'operations': last_ops})
