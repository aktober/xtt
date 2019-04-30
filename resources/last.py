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
        if not currency and not number:
            op = models.Operations.query.order_by(-models.Operations.requested_time)\
                .first()
            if op:
                last_ops.append(op.to_dict())

        elif not currency and number:
            ops = models.Operations.query.order_by(-models.Operations.requested_time)\
                .limit(number)
            for op in ops:
                last_ops.append(op.to_dict())

        elif currency and not number:
            op = models.Operations.query.filter_by(currency=currency) \
                .order_by(-models.Operations.requested_time) \
                .first()
            if op:
                last_ops.append(op.to_dict())

        else:
            ops = models.Operations.query.filter_by(currency=currency) \
                .order_by(-models.Operations.requested_time) \
                .limit(number)
            for op in ops:
                last_ops.append(op.to_dict())

        return jsonify({'operations': last_ops})
