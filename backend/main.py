from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai_service import analyze_hair

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze/")
async def analyze_images(
    front: UploadFile = File(...),
    top: UploadFile = File(...),
    back: UploadFile = File(...)
):
    files = [front, top, back]

    for file in files:
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Only images allowed")

    result = analyze_hair(files)
    return result