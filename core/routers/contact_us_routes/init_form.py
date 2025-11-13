from fastapi import APIRouter
from core.routers.contact_us_routes.conatct_form_routes import contact_form_api

contact_form_route = APIRouter()

contact_form_route.include_router(contact_form_api)
