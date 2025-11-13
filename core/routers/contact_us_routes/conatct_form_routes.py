from fastapi import APIRouter, Form
from pydantic import EmailStr
from core.services.contact_us.contact_us import contact_us_service

contact_form_api = APIRouter()


@contact_form_api.post("/submit-contact-form")
async def submit_contact_form(name: str = Form(...), email: EmailStr = Form(...), phone_no: str = Form(...), service_selected: list[str] = Form(...), Message: str = Form(...)):
    response = await contact_us_service(name, email, phone_no, service_selected, Message)
    return response
