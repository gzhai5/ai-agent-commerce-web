from fastapi import APIRouter, HTTPException, Depends
from loguru import logger
from app.message.message_service import message_service


# define the router
router = APIRouter(prefix="/message", tags=["Message"])

@router.get("/products", response_description="List all products", status_code=200)
async def list_products():
    try:
        products = message_service.list_products()
        return products
    except HTTPException as http_e:
        logger.error(f"ERROR: HTTPException occurred when listing products: {http_e.detail}")
        raise http_e
    except Exception as e:
        logger.error(f"ERROR: An unexpected error occurred when listing products: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred when listing products") from e
