from datetime import datetime

class Bill:
    def __init__(self, bill_id, tenant_id, room_id, base_rent, billing_month):
        self.bill_id = bill_id
        self.tenant_id = tenant_id
        self.room_id = room_id
        self.base_rent = base_rent
        self.billing_month = billing_month
        self.utilities_cost = 0
        self.parking_fee = 0
        self.management_fee = 0
        self.total_amount = base_rent
        self.paid_amount = 0
        self.status = 'pending'
        self.created_at = datetime.utcnow()

    def add_charge(self, charge_type, amount):
        if charge_type == 'utilities':
            self.utilities_cost = amount
        elif charge_type == 'parking':
            self.parking_fee = amount
        elif charge_type == 'management':
            self.management_fee = amount
        self.calculate_total()
        return self

    def calculate_total(self):
        self.total_amount = self.base_rent + self.utilities_cost + self.parking_fee + self.management_fee
        return self.total_amount

    def record_payment(self, payment_amount):
        self.paid_amount += payment_amount
        remaining = self.total_amount - self.paid_amount
        if remaining <= 0:
            self.status = 'paid'
        elif self.paid_amount > 0:
            self.status = 'partial'
        return self

class Payment:
    def __init__(self, payment_id, bill_id, amount, payment_method):
        self.payment_id = payment_id
        self.bill_id = bill_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_date = datetime.utcnow()
        self.status = 'completed'

class BillingTemplate:
    def __init__(self, template_id, template_name):
        self.template_id = template_id
        self.template_name = template_name
        self.base_rent = 0
        self.utilities_cost = 0
        self.parking_fee = 0
        self.management_fee = 0
        self.billing_frequency = 'monthly'
        self.due_day = 1
        self.is_active = True
        self.created_at = datetime.utcnow()