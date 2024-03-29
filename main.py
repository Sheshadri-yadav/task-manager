

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,Request

from routes.manager import manager

from fastapi import FastAPI



app = FastAPI()


templates: Jinja2Templates = Jinja2Templates(directory="templates")
# Mount the directory containing your static files (HTML, CSS, JavaScript)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(manager)


@app.get("/")
async def landing_page(request:Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )


