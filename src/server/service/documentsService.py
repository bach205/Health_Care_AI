import shutil
import os
from pathlib import Path
from src.server.model.documentsModel import save_documents_to_database
UPLOAD_FOLDER = Path(__file__).parent.parent.parent.parent / "documents"

async def save_documents(file,user_id):
    # Tạo đường dẫn tuyệt đối để lưu file
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)

    # Lưu file, wb la method write + binary (lam viec voi file nhi phan)
    with open(file_location, "wb") as buffer:
        #copy file object of file sang file object of buffer, (chung quy lai la ghi noi dung file vao buffer)
        shutil.copyfileobj(file.file, buffer)
    
    #save documents to database
    save_documents_to_database(file,file_location,user_id)

    return file