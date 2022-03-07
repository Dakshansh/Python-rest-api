import os
from config import db
from models import Student




if os.path.exists("student.db"):
    os.remove("student.db")

# Create the database
db.create_all()
