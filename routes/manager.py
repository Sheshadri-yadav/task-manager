from fastapi import APIRouter, File, UploadFile, HTTPException, Response, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from functions.functions import completed_tasks, incomplete_tasks, all_tasks, insert_query, update_tasks, delete_task
from jinja2 import Template

from models.model import Tasks

manager = APIRouter()

templates = Jinja2Templates(directory="templates")
"""
@manager.get("/all_task")
async def get_all_data():
    newdocs = []

    try:
        result = all_tasks()

        for doc in result:
            newdocs.append({
                "task_id": doc["task_id"],
                "task_title": doc["task_title"],
                "task_desc": doc["task_desc"],
                "due_date": doc["due_date"],
                "due_time": doc["due_time"],
                "task_status": doc["task_status"]
            })

        return newdocs[::-1]
    except Exception as e:
        print("Error occurred while fetching all tasks:", e)
        return {"error": "Failed to fetch tasks"}
"""


@manager.post("/add_new_task")
async def new_task(request: Request):
    form_data = await request.form()
    task_title = form_data.get("task_title")
    task_desc = form_data.get("task_desc")
    due_date = form_data.get("due_date")
    due_time = form_data.get("due_time")

    if not all([task_title, task_desc, due_date, due_time]):
        return {"error": "All fields are required"}

    try:
        print("hello")
        insert_query(task_title, task_desc, due_date, due_time, False)
        # Perform database insertion or any other operations here
        return {"success"}

    except Exception as e:
        print(f"Error occurred during insertion: {e}")
        return {"error": "Failed to add task"}


@manager.get('/completed_tasks')
async def completed_task():
    newdocs = []

    result = completed_tasks()

    for doc in result:
        newdocs.append({
            "task_id": doc[0],
            "task_title": doc[1],
            "task_desc": doc[2],
            "due_date": doc[3],
            "due_time": doc[4],
            "task_status": doc[5]
        })

    return newdocs[::-1]


@manager.get('/incomplete_tasks')
async def incomplete_task():
    newdocs = []

    result = incomplete_tasks()

    for doc in result:
        newdocs.append({
            "task_id": doc[0],
            "task_title": doc[1],
            "task_desc": doc[2],
            "due_date": doc[3],
            "due_time": doc[4],
            "task_status": doc[5]
        })

    return newdocs[::-1]


@manager.put("/update/{task_id}")
async def update_task(task_id: int):
    try:
        update_tasks(task_id)
        tasks = all_tasks()
        return {"success": True, "tasks": tasks[::-1]}  # Return updated tasks
    except:
        return {"success": False}


@manager.delete("/delete/{task_id}")
async def delete_record(task_id: int):
    try:
        delete_task(task_id)
        tasks=all_tasks()
        return {"success": True, "tasks": tasks[::-1]}  # Return updated tasks
    except:
        return {"success": False}


# to display all the tasks
@manager.get("/all_tasks")
async def display_all_tasks(request: Request):
    try:
        tasks = all_tasks()

        return templates.TemplateResponse("template.html", {"request": request, "tasks": tasks[::-1]})
    except Exception as e:
        print("Error occurred while fetching all tasks:", e)
        return {"error": "Failed to fetch tasks"}


# for displaying the landing page of input adding tasks
@manager.get("/add_new_tasks")
async def adding_task_page(request: Request):
    return templates.TemplateResponse("add_tasks.html", {"request": request})


# for displaying the landing page of input adding tasks
@manager.get("/edit_tasks")
async def display_all_tasks(request: Request):
    try:
        tasks = all_tasks()

        return templates.TemplateResponse("edit_tasks.html", {"request": request, "tasks": tasks[::-1]})
    except Exception as e:
        print("Error occurred while fetching all tasks:", e)
        return {"error": "Failed to fetch tasks"}
