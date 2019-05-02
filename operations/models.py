from sqlalchemy.dialects.mysql.base import MSDouble

from app import db, ma
from datetime import datetime


class Operations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(3), nullable=False)
    amount = db.Column(MSDouble(15, 8), nullable=False)
    price = db.Column(MSDouble(15, 8))
    final_amount = db.Column(MSDouble(15, 8))
    requested_time = db.Column(db.DateTime, nullable=False,
                               default=datetime.utcnow)

    def to_dict(self):
        return {'id': self.id,
                'currency': self.currency,
                'amount': float(self.amount),
                'price': float(self.price),
                'final_amount': float(self.final_amount),
                'requested_time': self.requested_time}

    def __str__(self):
        return f"Operation ({self.id}): currency:{self.currency}; amount:{self.amount}; " \
               f"price:{self.price}; final_amount ($):{self.final_amount}"


class OperationSchema(ma.Schema):
    class Meta:
        fields = ("id", "currency", "amount", "price", "final_amount",
                  "requested_time")

    amount = ma.Float()
    price = ma.Float()
    final_amount = ma.Float()


operation_schema = OperationSchema()
operations_schema = OperationSchema(many=True)
