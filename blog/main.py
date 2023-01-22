from fastapi import FastAPI

import dish_router
import menu_router
import submenu_router

app = FastAPI()

app.include_router(menu_router.router)
app.include_router(submenu_router.router)
app.include_router(dish_router.router)
