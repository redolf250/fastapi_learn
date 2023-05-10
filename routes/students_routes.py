from fastapi import APIRouter, status
from schema.student import Student
from service.student_service import *

student_routes = APIRouter()

@student_routes.get('/',tags=['Get'])
async def test():
    return "hello world"

@student_routes.post('/api/v1/student/registor',tags=['Post'], status_code=status.HTTP_201_CREATED)
async def save_student(_student: Student):
    save_student_(_student)
    return _student

@student_routes.get('/api/v1/students',tags=['Get'],status_code=status.HTTP_302_FOUND)
async def fetch_all_students():
    _student=get_all_students()
    return _student
  
@student_routes.get('/api/v1/students/{student_id}',tags=['Get'])
async def fetch_student_by_id(student_id: int):
    _student=get_student_by_id(student_id)
    return _student

@student_routes.delete('/api/v1/students/{student_id}',tags=["Delete"])
async def remove_student_by_id(student_id: int):
    delete_student_by_id(student_id)
    
@student_routes.put('/api/v1/students/{student_id}',tags=['Put'])
async def remove_student_by_id(student_id: int,_student: Student):
    update_student_by_id(student_id,_student)

