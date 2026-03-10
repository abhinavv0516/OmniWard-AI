from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from app.services.image_verification import verify_change
from app.services.video_generator import generate_video
app = FastAPI()

UPLOAD_FOLDER = "storage"
VIDEO_FOLDER = "storage/generated_videos"

os.makedirs("storage/before_images", exist_ok=True)
os.makedirs("storage/after_images", exist_ok=True)
os.makedirs(VIDEO_FOLDER, exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "OmniWard AI Backend Running"}


@app.post("/upload")
async def upload_images(
    before: UploadFile = File(...),
    after: UploadFile = File(...)
):

    before_path = f"storage/before_images/{before.filename}"
    after_path = f"storage/after_images/{after.filename}"

    with open(before_path, "wb") as buffer:
        shutil.copyfileobj(before.file, buffer)

    with open(after_path, "wb") as buffer:
        shutil.copyfileobj(after.file, buffer)

    verified = verify_change(before_path, after_path)

    if not verified:
        return {"status": "No improvement detected"}

    video_path = generate_video(before_path, after_path)

    return {
        "status": "Improvement verified",
        "video": video_path
    }