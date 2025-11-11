from fastapi import APIRouter
from core.routers.job_submissions_routes.job_submission import job_submission

job_routes = APIRouter()

job_routes.include_router(job_submission)
