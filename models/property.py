from datetime import datetime

class Building:
    def __init__(self, building_id, name, address):
        self.building_id = building_id
        self.name = name
        self.address = address
        self.created_at = datetime.utcnow()
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)
        return self

class Room:
    def __init__(self, room_id, building_id, room_number, area, monthly_rent):
        self.room_id = room_id
        self.building_id = building_id
        self.room_number = room_number
        self.area = area
        self.monthly_rent = monthly_rent
        self.status = 'available'
        self.created_at = datetime.utcnow()
        self.tenants = []

    def occupy(self, tenant_id):
        self.tenants.append(tenant_id)
        self.status = 'occupied'
        return self

    def vacate(self, tenant_id):
        if tenant_id in self.tenants:
            self.tenants.remove(tenant_id)
        if not self.tenants:
            self.status = 'available'
        return self

class Facility:
    def __init__(self, facility_id, building_id, facility_name, facility_type):
        self.facility_id = facility_id
        self.building_id = building_id
        self.facility_name = facility_name
        self.facility_type = facility_type
        self.status = 'active'
        self.created_at = datetime.utcnow()