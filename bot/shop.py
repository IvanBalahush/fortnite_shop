import logging

import requests

from fortnite_shop.config.settings import FORTNITE_API_KEY, FORTNITE_API_URL
from fortnite_shop.bot.utils import trim_line

logger = logging.getLogger(__name__)

async def get_fortnite_shop():
    """Gets the current fortnite shop from API."""
    headers = {"Authorization": FORTNITE_API_KEY}
    try:
        response = requests.get(FORTNITE_API_URL, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        items = data.get("data", {}).get("entries", [])
        shop_text = "Fortnite Shop Items Today:\n\n"
        for item in items:
            if 'offetTag' in item:
                continue
            name = trim_line(item.get('devName', 'Unknown'))
            price = item.get('finalPrice', 'N/A')
            shop_text += f"{name} - {price} V-bucks\n"
        return shop_text.strip() or "No available items in the shop today."
    except requests.RequestException as e:
        logger.error(f"Fortnite API error: {e}")
        return "Could not return data of the shop. Try later."