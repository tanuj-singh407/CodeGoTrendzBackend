import re
import os
from core.config import get_settings

settings = get_settings()


async def sanitize_filename(name: str):

    name = re.sub(r'[^\w\-_.]', '_', name)
    name = re.sub(r'_+', '_', name)

    root, ext = (os.path.splitext(name))

    first_name = root.strip("_")

    if (len(first_name) > settings.MAX_LENGTH_FILENAME):
        first_name = first_name[:settings.MAX_LENGTH_FILENAME]

    final_name = f"{first_name}{ext}"

    return final_name