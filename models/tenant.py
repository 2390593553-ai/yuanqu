from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tenant(db.Model):
    """Tenant model"""
    __tablename__ = 'tenants'
    
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    company_name = db.Column(db.String(255))
    business_type = db.Column(db.String(255))
    id_number = db.Column(db.String(50))
    id_type = db.Column(db.String(50))  # passport, national_id, business_license
    contact_person = db.Column(db.String(255))
    contact_phone = db.Column(db.String(20))
    status = db.Column(db.String(50), default='active')  # active, inactive, former
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    contracts = db.relationship('Contract', backref='tenant', lazy=True, cascade='all, delete-orphan')
    bills = db.relationship('Bill', backref='tenant', lazy=True)
    
    def __repr__(self):
        return f'<Tenant {self.name}>'

class Contract(db.Model):
    """Contract model"""
    __tablename__ = 'contracts'
    
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)
    contract_number = db.Column(db.String(100), unique=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    monthly_rent = db.Column(db.Float, nullable=False)
    deposit = db.Column(db.Float)
    status = db.Column(db.String(50), default='active')  # active, expired, terminated
    terms_and_conditions = db.Column(db.Text)
    signed_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Contract {self.contract_number}>'
