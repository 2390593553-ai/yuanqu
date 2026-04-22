from datetime import datetime

class MaintenanceTicket:
    def __init__(self, ticket_id, description, created_at=None):
        self.ticket_id = ticket_id
        self.description = description
        self.created_at = created_at or datetime.utcnow()

class MaintenanceSchedule:
    def __init__(self, schedule_id, ticket_id, scheduled_time):
        self.schedule_id = schedule_id
        self.ticket_id = ticket_id
        self.scheduled_time = scheduled_time
        self.completed = False

    def mark_completed(self):
        self.completed = True
        return datetime.utcnow()  
