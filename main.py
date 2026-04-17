from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/analyze")
async def analyze_video(file: UploadFile = File(...)):
    video_path = f"{UPLOAD_FOLDER}/{file.filename}"
    
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "status": "success",
        "highlights": [750, 3310, 4245]
    }
