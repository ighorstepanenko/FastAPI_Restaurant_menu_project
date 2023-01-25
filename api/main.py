from fastapi import FastAPI
from database import engine
import models

from routers import menu_router, submenu_router, dish_router

app = FastAPI(debug=True)
models.Base.metadata.create_all(bind=engine)

app.include_router(menu_router.router)
app.include_router(submenu_router.router)
app.include_router(dish_router.router)
