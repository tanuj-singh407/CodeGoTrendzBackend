import os
import shutil
from core.utils.sanitize_name import sanitize_filename
from fastapi import HTTPException
from pathlib import Path
from core.database.mongodb import job_applications
from core.utils.date_time import current_date_time


async def job_application_submission(name: str, address: str, job_profile: str, resume):

    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400, detail="Only PDF files are allowed")

    final_name = await sanitize_filename(resume.filename)

    data = await current_date_time()

    upload_dirs = "uploads/resumes"

    os.makedirs(upload_dirs, exist_ok=True)

    file_path = os.path.join(upload_dirs, final_name)

    with open(file_path, "wb") as f:
        contents = await resume.read()
        f.write(contents)

    resume_path = Path("uploads")/f'resumes'/final_name

    applications = {
        "name": name,
        "address": address,
        "job_profile": job_profile,
        "resume_path": str(resume_path),
        "submitted_date": str(data["current_date"]),
        "submitted_time": data["current_time"]
    }

    response = await job_applications.insert_one(applications)

    if (response.acknowledged == True):
        return {"message": "Your Job Application Submitted Successfully"}
