from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.routers.subscription import router as subscriptions_router
from src.routers.payment_history import router as payment_history_router

#Se crea la instancia de la API
app = FastAPI(
    title= "Subscription gestor API",
    description= "API for subscription management",
    version="1.0.0"
)

#Configuracion de los middlewares globales
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(subscriptions_router)
app.include_router(payment_history_router)
#Ruta de prueba
@app.get("/")
def read_root():
    return{"message":"Si funciona carajo"}


#Arranque del servidor
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)