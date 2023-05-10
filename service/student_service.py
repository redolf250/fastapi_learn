from config.config import conn
from schema.student import Student
from model.index import student
from fastapi import File, UploadFile

def save_student_(_student: Student):
    conn.execute(student.insert().values(
        firstname=_student.firstname,
        lastname=_student.lastname,
        mail=_student.mail
    ))
    return _student

def get_all_students():
    _student=conn.execute(student.select()).fetchall()
    return _student

def get_student_by_id(student_id):
    _student=conn.execute(student.select().where(student.c.id==student_id)).fetchone()
    return _student

def delete_student_by_id(student_id):
    conn.execute(student.delete().where(student.c.id==student_id)).fetchone()

def update_student_by_id(student_id: int,_student: Student):
    conn.execute(student.update().values(
        firstname=_student.firstname,
        lastname=_student.lastname,
        mail=_student.mail
    ).where(student.c.id==student_id))
    return "Success"

def upload_file_(file: UploadFile = File(...)):
    return {"file": file.filename, "size": file.read}
    

