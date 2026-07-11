from fastapi import HTTPException, Request, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.config.supabase import supabase

#Busca el encabezado Bearer
security = HTTPBearer()

async def protect_route(credentials: HTTPAuthorizationCredentials = Security(security)):
    #Se extrae el token 
    token = credentials.credentials

    try:

        #Supabase valida el token, si es real y de quien es
        response = supabase.auth.get_user(token)
        user = response.user

        #Si Supabase no encuentra ningun usuario con el token
        if not user:
            raise HTTPException(status_code=401, detail="Token invalido o expirado.")
        
        #Si todo sale bien se develve el usuario par que la ruta lo use
        return user
    except Exception as e:
        #Si ocurre cualquier error en el proceso se bloquea la peticon
        raise HTTPException(status_code=401, detail="Token invalaido o expirado")