from src.config.supabase import supabase
from src.middlewares.auth_middlewares import protect_route
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from datetime import date

router = APIRouter(
    tags= ["Subscriptions history"],
    dependencies= [Depends(protect_route)]
)
'''
class HistorySubscription(BaseModel):
    payment_date
'''
@router.get(
    "/getHistorySubscription",
    summary= "History of any subscription",
    response_description= "Subscription history successfully obtained."
)
def getHistory(id_user: str, user = Depends(protect_route)):
    try:
        response = supabase \
            .table("payment_history")\
            .select("*")\
            .eq("id_user", user.id)\
            .execute()
        if not response.data:
            raise HTTPException(
                status_code=404, 
                detail=f"Not subscription found by {id_user}."
                )
        
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Server error.")