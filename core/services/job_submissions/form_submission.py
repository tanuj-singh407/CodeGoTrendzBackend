import os
import shutil
from core.utils.sanitize_name import sanitize_filename
from fastapi import HTTPException


async def job_application_submission(name: str, address: str, job_profile: str, resume):

    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400, detail="Only PDF files are allowed")

    final_name = await sanitize_filename(resume.filename)

    upload_dirs = "uploads/resumes"

    os.makedirs(upload_dirs, exist_ok=True)

    file_path = os.path.join(upload_dirs, final_name)

    with open(file_path, "wb") as f:
        contents = await resume.read()
        f.write(contents)

        # print(response, "final_name")
