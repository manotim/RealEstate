from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import ENUM



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(ENUM('tenant', 'landlord', 'admin', name='user_role', create_type=False), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))
    agreement_pdf = db.Column(db.String(255))
    payments = db.relationship('Payment', backref='tenant', lazy=True)
    water_bills = db.relationship('WaterBill', backref='tenant', lazy=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Landlord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    apartments = db.relationship('Apartment', backref='landlord', lazy=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    landlord_id = db.Column(db.Integer, db.ForeignKey('landlord.id'), nullable=False)
    houses = db.relationship('House', backref='apartment', lazy=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'), nullable=False)
    number = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.Enum('available', 'booked', name='house_status'), default='available', nullable=False) # Added name
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_id = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.Enum('pending', 'successful', 'failed', name='payment_status'), default='pending', nullable=False) # Added name
    water_bill_id = db.Column(db.Integer, db.ForeignKey('water_bill.id'), nullable=True)
    date_paid = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class WaterBill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=False)
    units_consumed = db.Column(db.Float, nullable=False)
    amount_due = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum('pending', 'paid', name='water_bill_status'), default='pending', nullable=False) # Added name
    date_issued = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)