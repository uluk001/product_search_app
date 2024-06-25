import os
import requests
from PIL import Image
from io import BytesIO
from loguru import logger

IMAGE_URLS = [
    "https://w.forfun.com/fetch/74/74739e1770f31cdbfdde99cc0b2925d3.jpeg",
    "https://i.pinimg.com/originals/de/a8/4d/dea84d584888669b068a94d4f732156c.jpg",
    "https://w.forfun.com/fetch/73/73aa25921c66f5a77e44d6e653ebc33b.jpeg",
    "https://i.pinimg.com/originals/3f/05/79/3f0579a4c16909ce1a8d367b23aaa611.jpg",
]


def download_images(save_dir="app/static/images"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for idx, url in enumerate(IMAGE_URLS):
        logger.info(f"Downloading image {idx + 1}/{len(IMAGE_URLS)}")
        response = requests.get(url)
        logger.info(f"Saving image {idx + 1}/{len(IMAGE_URLS)}")
        img = Image.open(BytesIO(response.content))
        logger.info(f"Image size: {img.size}")
        img.save(os.path.join(save_dir, f"image_{idx}.jpg"))
