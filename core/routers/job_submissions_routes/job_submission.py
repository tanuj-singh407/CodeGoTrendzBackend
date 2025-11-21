from fastapi import APIRouter, Form, File, UploadFile
from core.services.job_submissions.form_submission import job_application_submission

job_submission = APIRouter()


@job_submission.post("/submit-job-application")
async def submit_job_application(name: str = Form(...), email: str = Form(...), jobProfile: str = Form(...), cv: UploadFile = File(...)):
    response = await job_application_submission(name, email, jobProfile, cv)
    return response
