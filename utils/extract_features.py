import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
import os
import pickle
from PIL import Image


def extract_features(image_path, model, transform):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        features = model(image).flatten().numpy()
    return features


def save_features(image_dir="data/images", feature_file="data/features.pkl"):
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
    for image_name in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_name)
        features[image_name] = extract_features(image_path, model, transform)
    with open(feature_file, "wb") as f:
        pickle.dump(features, f)
