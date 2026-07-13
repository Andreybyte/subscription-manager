from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import date
from src.config.supabase import supabase

router = APIRouter(tags=["Subscriptions"])

class SubscriptionSchema(BaseModel):
    #Modelo de datos
    id_user: str = Field(..., example="8eea60f9-3e3c-459a-a3b3-ade3d37f2c06")
    category: str = Field(..., example="Streaming")
    name_subscription: str = Field(..., example="Netflix")
    details_subscription: str = Field(..., example="None")
    start_date : date = Field(..., example= "2026-08-07")
    next_payment: date = Field(..., example= "2026-09-07")
    billing_amount : float = Field(..., example= 8500.0)

class SubscriptionUpdateSchema(BaseModel):
    #Modelo de datos para actulizar alguna subscripcion
    category: str | None = Field(None, example="Streaming")
    name_subscription: str | None  = Field(None, example="Netflix")
    details_subscription: str | None  = Field(None, example="None")
    start_date : date | None  = Field(None, example= "2026-08-07")
    next_payment: date | None  = Field(None, example= "2026-09-07")
    billing_amount : float | None  = Field(None, example= 8500.0)

@router.post(
        "/subscription",
        summary="Create new supscription",
        response_description= "The supscription was created succesully."
        )
def create_subscription(payload: SubscriptionSchema):
    try:
        #Se convierte el payload en un dicconario limpio
        data_to_insert = payload.model_dump( mode="json")
        response = supabase.table("subscription").insert(data_to_insert).execute()

        return {
            "message" : "Subscription added successfully.",
            "data" : response.data
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Server error.")
    
#Metodo para actualizar subscripciones
@router.patch(
    "/UpdateSubscription",
    summary="Update Subscription",
    response_description= "The subscription was updated."
)
def updateSubscription(id_subscription: str, payload: SubscriptionUpdateSchema):
    try:
        
        data_to_update = payload.model_dump(exclude_unset=True, mode="json")

        if not data_to_update:
            raise HTTPException(status_code=400, detail="No fields provide to update")
        
        response = supabase.table("subscription").update(data_to_update).eq("id_subscription", id_subscription).execute()

        return {
            "message" : "Subscription updated successfully",
            "data" : response.data
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Server error")

@router.get(
    "/getSubscription",
    summary="Get any subscription",
    response_description= "Subscription data"
)
def getSubscription(id_user: str):
    try:
        response = supabase.table("subscription").select("*").eq("id_user", id_user).execute()
        if not response.data:
            raise HTTPException(
                status_code=404,
                detail=f"Subscription of user id '{id_user} not found."
            )

        return {
            "message" : "Subscription data",
            "data": response.data
        }
    
    except HTTPException as http_error:
        raise http_error 

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Server error")
    
@router.delete(
    "/deleteSubscription",
    summary="Delete any subscription",
    response_description="Subscription deleted successfully."
)
def deleteSubscription(id_subscription: str):
    try:
        response = supabase.table("subscription").delete().eq("id_subscription", id_subscription).execute()


    
    except HTTPException as http_error:
        print(http_error)
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Server Error")
    
    if not response or not response.data:
        raise HTTPException(
            status_code=404,
            detail="No subscription found with the provide id."
        )
        
    return {
        "message": "Subscription deleted succesfully.",
        "delete_data" : response.data[0]
    }