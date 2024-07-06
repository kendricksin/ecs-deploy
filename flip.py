from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image
import io

flip = FastAPI()

@flip.post("/flip_image")
async def flip_image(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")
    
    try:
        img = Image.open(file.file)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")
    
    # Flip the image vertically
    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    
    # Save the flipped image to a bytes buffer
    img_byte_arr = io.BytesIO()
    flipped_img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return StreamingResponse(img_byte_arr, media_type="image/png")

# Remove the if __name__ == "__main__": block if it exists