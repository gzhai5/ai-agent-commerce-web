from loguru import logger
from datetime import datetime
from app.message.database.data import products as all_products

class MessageService:
    def __init__(self):
        pass

    def list_products(self):
        logger.info(f"INFO: Listing all products at {datetime.utcnow().isoformat()}Z")
        return all_products


message_service = MessageService()