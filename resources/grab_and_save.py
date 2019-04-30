import json

import requests
from flask import jsonify
from flask_restful import Resource, reqparse

from app import db
from config import OER_API_KEY
from operations import models

URL = 'https://openexchangerates.org/api/latest.json'


class GrabSaveResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('currency', location='form', type=str, required=True)
        parser.add_argument('amount', location='form', type=float, required=True)

        args = parser.parse_args(strict=True)
        currency = args['currency'].upper()
        amount = args['amount']

        params = {'app_id': OER_API_KEY, 'symbols': currency}
        r = requests.get(URL, params)
        json_data = json.loads(r.content)

        currency_rate = json_data['rates'].get(currency)
        if currency_rate:
            final_amount = (1 / currency_rate) * amount
            operation = models.Operations(currency=currency,
                                          amount=amount,
                                          price=currency_rate,
                                          final_amount=final_amount)
            db.session.add(operation)
            db.session.commit()

            return jsonify({'operation': str(operation)})
        else:
            return jsonify({'message': f'Currency {currency} not found'})
