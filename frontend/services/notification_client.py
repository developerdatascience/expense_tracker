from services.api_client import APIClient


class NotificationClient:

    @staticmethod
    def get_notifications():
        return APIClient.get("/notifications/").json()