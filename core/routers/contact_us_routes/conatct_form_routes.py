from fastapi import APIRouter, Form, HTTPException
from pydantic import EmailStr
from core.services.contact_us.contact_us import contact_us_service

contact_form_api = APIRouter()


@contact_form_api.post("/submit-contact-form")
async def submit_contact_form(name: str = Form(...), email: EmailStr = Form(...), phone_no: int = Form(...), service_selected: list[str] = Form(...), Message: str = Form(...)):

    try:
        response = await contact_us_service(name, email, phone_no, service_selected, Message)
        return response
    except Exception as e:
        raise HTTPException(
            detail=f"Unable to submit the form. Error-{str(e)}")
