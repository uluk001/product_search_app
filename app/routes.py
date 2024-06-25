from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.image_processing import extract_features
from utils.search import search_similar_images

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@router.post("/search")
async def search(file: UploadFile = File(...)):
    image_bytes = await file.read()
    query_feature = extract_features(image_bytes)
    similar_images = search_similar_images(query_feature)
    return {"results": similar_images}


router.mount("/static", StaticFiles(directory="app/static"), name="static")
