import uvicorn
from fastapi import FastAPI
from app.routes import router
from fastapi.staticfiles import StaticFiles
from utils.download_images import download_images
from utils.extract_features import save_features

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)


def main():
    download_images()
    save_features()
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
