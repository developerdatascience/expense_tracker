from app.models.notification import Notification


class NotificationService:
    def __init__(self, db):
        self.db = db
    
    def create(self, user_id, message, type_):
        notif = Notification(user_id=user_id, message=message, type=type_)
        self.db.add(notif)
        self.db.commit()
        self.db.refresh(notif)
        return notif
    
    def get_all(self, user_id):
        return self.db.query(Notification) \
        .filter(Notification.user_id == user_id)\
        .order_by(Notification.created_at.desc())\
        .all()