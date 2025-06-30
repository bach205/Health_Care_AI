from fastapi.responses import StreamingResponse
import time
from fastapi import APIRouter,FastAPI, UploadFile, File,Form
from pydantic import BaseModel
from src.server.service.documentsService import save_documents
class response(BaseModel):
    status:int
    message:dict
router = APIRouter()

@router.post("/upload")
async def document_processing(file: UploadFile = File(...),user_id: int = Form(...)):
    """
    Save documents.
    """
    result = await save_documents(file,user_id)
    return response(
        status=201,
        message={"filename": result.filename, "content_type": result.content_type}
    )

def generate_sse():
    for i in range(10):
        time.sleep(1)  # Giả lập xử lý
        yield f"data: Thông báo số {i + 1}\n\n"
    yield "data: Xử lý hoàn tất!\n\n"

@router.get("/stream_response")
def sse_endpoint():
    return StreamingResponse(generate_sse(), media_type="text/event-stream")