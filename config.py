from fastapi import FastAPI
from routers import users


app = FastAPI()
app.include_router(users.router, tags=['users'])
