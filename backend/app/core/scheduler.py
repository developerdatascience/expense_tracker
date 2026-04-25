from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.db.session import SessionLocal
from app.models.bill import Bill
from app.services.notification_service import NotificationService

scheduler = BackgroundScheduler()

def check_bills():
    db = SessionLocal()

    bills = db.query(Bill).all()
    notif_service = NotificationService(db)

    today = datetime.now().date()

    for bill in bills:
        if bill.due_date.date() == today:
            notif_service.create(
                bill.user_id,
                f"Bill due: {bill.name}",
                "bill_due"
                )
    
    db.close()


def start_scheduler():
    scheduler.add_job(check_bills, "interval", hours=24)
    scheduler.start()