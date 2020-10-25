from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class Student(BaseModel):
	name : str
	subname : str
	age : int

class Course(BaseModel):
	name : str

class Mark(BaseModel):
	student : Student
	course : Course
	mark : int

@app.get('/')

def index():
	return {'key' : 'value'}

@app.get('/students')
def get_students():
	return db
@app.get('/students/{student_id}')
def get_student(student_id : int):
	return db[student_id-1]

@app.delete('/students/{student_id}')
def delete_student(student_id : int):
	db.pop(student_id-1)
	return {}

@app.post('/students/{student_id}')
def create_student(student : Student):
	db.append(student.dict())
	return db[-1]