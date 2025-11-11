import os
import shutil
from core.utils.sanitize_name import sanitize_filename
from fastapi import HTTPException


async def job_application_submission(name: str, address: str, job_profile: str, resume):

    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400, detail="Only PDF files are allowed")

    print(os.path.splitext(resume.filename), "------")

    final_name = await sanitize_filename(resume.filename)

    print(final_name, "final_name")
