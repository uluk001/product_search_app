import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
import os
import pickle
from PIL import Image
from loguru import logger


def extract_features(image_path, model, transform):
    logger.info(f"Opening image: {image_path}")
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        logger.info(f"Extracting features for image: {image_path}")
        features = model(image).flatten().numpy()
    return features


def save_features(image_dir="app/static/images", feature_file="data/features.pkl"):
    logger.info("Loading ResNet50 model with default weights")
    weights = ResNet50_Weights.DEFAULT
    model = resnet50(weights=weights)
    model.eval()
    transform = transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    features = {}
    logger.info(f"Processing images in directory: {image_dir}")
    for image_name in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_name)
        features[image_name] = extract_features(image_path, model, transform)
        logger.info(f"Features extracted for image: {image_name}")

    if features:  # Check if the features dictionary is not empty
        logger.info(f"Saving extracted features to file: {feature_file}")
        with open(feature_file, "wb") as f:
            pickle.dump(features, f)
        logger.info("Feature extraction and saving completed.")
    else:
        logger.warning(
            "No features were extracted. Check if the image directory is not empty."
        )
