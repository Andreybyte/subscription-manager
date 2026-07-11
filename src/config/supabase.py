import os
from dotenv import load_dotenv
from supabase import create_client, Client

#cargamos el archivo .env con las varibles
load_dotenv()

#Se leen las variables del archivo 
supabase_url = os.getenv("supabase_url")
supabase_rls = os.getenv("supabase_rls")

#Creamos el cliente de supabase
supabase: Client = create_client(supabase_url, supabase_rls)