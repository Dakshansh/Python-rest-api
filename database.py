import os
from config import db
from models import Student

# Data to initialize database with
"""
STUDENT = [
    {"sid": "Doug", "enrolled": True, "name": "D11", "classs": "class tenth", "age": "15", "des": "science guy",
     "fd": "2022-03-05T12:58:25.439Z"}
]
"""
# Delete database file if it exists currently
if os.path.exists("student.db"):
    os.remove("student.db")

# Create the database
db.create_all()
"""
# iterate over the PEOPLE structure and populate the database
for stu in STUDENT:
    s = Student(sid=stu.get("sid"), enrolled=stu.get("enrolled"), name=stu.get("name"), classs=stu.get("classs"),
                age=stu.get("age"), des=stu.get("des"), fd=stu.get("fd"))
    db.session.add(s)

db.session.commit()
"""