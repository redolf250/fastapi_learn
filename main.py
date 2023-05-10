from fastapi import FastAPI
from service.student_service import *
from routes.students_routes import *

app = FastAPI()
app.include_router(student_routes,tags=['students'])


   