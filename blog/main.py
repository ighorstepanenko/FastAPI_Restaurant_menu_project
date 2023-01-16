from fastapi import FastAPI
import schemas, models, database

app = FastAPI()

models.Base.metadata.create_all(database.engine)


@app.get('/menus')
def index():
    return 'Hello'


@app.post('/menus')
def create_menu(request: schemas.Menus):
    return request


@app.get('/menus/{menu_id}/submenus')
def index():
    return 'Hello'


@app.post('/menus/{menu_id}/submenus')
def create_menu(request: schemas.Submenus):
    return request


@app.get('/menus/{menu_id}/submenus/{submenu_id}/dishes')
def index():
    return 'Hello'


@app.post('/menus/{menu_id}/submenus/{submenu_id}/dishes')
def create_menu(request: schemas.Dishes):
    return request
