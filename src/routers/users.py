from src.config.supabase import supabase
from src.middlewares.auth_middlewares import protect_route
from datetime import date
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field

router = APIRouter(
    tags="User CRUD",
    Depends=[Depends(protect_route)]
)

class userBaseModel(BaseModel):
    name_user : str = Field(..., example="Andrey")
    last_name : str = Field(..., example="Upamecano")
    email_user : str = Field(..., example="andreysolis76@gmail.com")
    password_user : str = Field(..., example="TripleT2026")
    created_at : date = Field(..., example="07-08-2026")

class updateSubscriptionSchema(BaseModel):
    
    name_user : str | None = Field(None, example="Andrey")
    last_name : str | None = Field(None, example="Upamecano")
    email_user : str | None = Field(None, example="andreysolis76@gmail.com")
    password_user : str = Field(None, example="TripleT2026")
    created_at : date = Field(None, example="07-08-2026")
    
@router.post(
    "/signupUser",
    summary="Signup User"
    response_description="The user signup was successful."
)
def userSignup(payload = userBaseModel):
      
