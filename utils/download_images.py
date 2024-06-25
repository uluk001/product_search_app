import os
import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from loguru import logger

FILE_OF_IMAGE_URLS = "data/image_urls.txt"


def get_image_urls(file_path):
    with open(file_path, "r") as f:
        return f.readlines()


def download_images(save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    urls = get_image_urls(FILE_OF_IMAGE_URLS)
    for idx, url in enumerate(urls):
        logger.info(f"Downloading image from {url}")
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            logger.info(f"Downloaded image from {url}")
            img.save(os.path.join(save_dir, f"image_{idx}.jpg"))
        except UnidentifiedImageError as e:
            logger.error(f"Failed to identify image at {url}: {e}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed for {url}: {e}")
