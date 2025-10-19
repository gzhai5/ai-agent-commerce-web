import os, sys, time
import requests
import urllib.parse
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/app/')))
from mcp.server.fastmcp import FastMCP
from loguru import logger
from app.servers.decision.utils import openai_utils



mcp = FastMCP(
    name = "Decision",
    description = "High-Level Check on decisions for users' queries",
    )

@mcp.tool()
def detect_if_user_want_chat(query: str) -> str:
    """
    Based on the user query, check if the user wants to do any chat with us.
    This kind of chat could be very basic communication, e.g. "What is your name?" or "What can you do?"
    This tool checks if the query matches the purpose of doing a chat and returns a response accordingly.
    Only use this tool if the user query matches the purpose of doing a chat.
    
    Args:
        query: The user query
    """
    logger.info(f"⛏ <Tool Level> Tool: user_want_chat, Query: {query}")
    return ""

@mcp.tool()
def detect_if_user_want_to_get_product_recommendation(query: str):
    """
    Based on the user query, check if the user wants to get any product recommendation.
    This tool checks if the query mentions any speicifc product or product category inside the commerce website product database.
    No image_url should be provided to this tool. If provided, please don't use this tool.
    Only use this tool if the user query matches the purpose of getting a product recommendation.

    Args:
        query: The user query that indicates interest in getting a product recommendation
    """
    logger.info(f"⛏ <Tool Level> Tool: user_want_to_get_product_recommendation, Query: {query}")
    try:
        response = requests.get(f"http://backend-server:8000/message/products")
        data = response.json()
        return {
            "all_products_details": data,
            "suggested_answer": "Here are some products you might be interested in. Please let me know if you would like more information about any of them."
        }
    except requests.RequestException as e:
        logger.error(f"⛏ <Tool Level> Tool: user_want_to_get_product_recommendation, Failed to retrieve product information: {e}")
        return {
            "text": "An error occurred while retrieving product information.",
            "error": str(e)
        }

@mcp.tool()
def detect_if_user_want_to_use_image_to_search_product(query: str, image_url: str) -> dict:
    """
    Decide if we should run an image-based product search and, if so, return
    the image description and candidate product details.
    e.g., "Find me products like this" or "What is this product?".

    Args:
        query: The user query that indicates interest in doing an image-based product search
        image_url: The URL of the image provided by the user for product search

    Returns:
        dict: {
            "image_description": str | None,
            "products": list | None,            # list of product dicts
        }
    """
    print(f"⛏ Tool: image-based search | Query: {query} | Image: {image_url}", file=sys.stderr)
    # Validate inputs early
    if not (query and isinstance(query, str)):
        return {"ok": False, "reason": "Empty query.", "image_description": None, "products": None, "suggested_answer": None}
    if not (image_url and isinstance(image_url, str) and image_url.startswith(("http://", "https://"))):
        return {"ok": False, "reason": "Missing or invalid image_url.", "image_description": None, "products": None, "suggested_answer": None}

    logger.info(f"⛏ Tool: image-based search | Query: {query} | Image: {image_url}")

    # Step 1: Ask model to describe the image (with bounded polling)
    try:
        description = openai_utils.openai_model_analyze_image(text=query, image_url=image_url)
    except Exception as e:
        logger.exception("Failed to create OpenAI model response")
        return {"ok": False, "reason": f"OpenAI create error: {e}", "image_description": None, "products": None, "suggested_answer": None}
    logger.info(f"OpenAI image description: {description!r}")

    # Step 2: Fetch products
    try:
        response = requests.get(f"http://backend-server:8000/message/products")
        data = response.json()
        return {
            "image_description": description,
            "products": data,
        }
    except requests.RequestException as e:
        logger.error(f"⛏ <Tool Level> Tool: user_want_to_use_image_to_search_product, Failed to retrieve product information: {e}")
        return {
            "text": "An error occurred while retrieving product information.",
            "error": str(e)
        }


if __name__ == "__main__":
    mcp.run(transport="stdio")