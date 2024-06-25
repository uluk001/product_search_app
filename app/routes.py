from fastapi import APIRouter, File, UploadFile
from utils.image_processing import extract_features
from utils.search import search_similar_images

router = APIRouter()


@router.post("/search")
async def search(file: UploadFile = File(...)):
    image_bytes = await file.read()
    query_feature = extract_features(image_bytes)
    similar_images = search_similar_images(query_feature)
    return {"results": similar_images}
