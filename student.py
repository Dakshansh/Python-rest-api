

from flask import abort, jsonify, request
from config import db
from models import Student, StudentSchema


def read_all():
    
    stud = Student.query.all()

  
    student_schema = StudentSchema(many=True)
    data = student_schema.dump(stud)
    return jsonify(data)


def read_one(sid):
    
    stud = Student.query.filter(Student.sid == sid).one_or_none()

  
    if stud is not None:

        
        student_schema = StudentSchema()
        data = student_schema.dump(stud)
        return jsonify(data)

   
    else:
        abort(
            404,
            "Student not found for Id: {sid}".format(sid=sid),
        )


def create():
   
    incoming_data = request.get_json()
    sid = incoming_data['sid']
    existing_student = (
        Student.query.filter(Student.sid == sid).one_or_none()
    )

   
    if existing_student is None:


        schema = StudentSchema()
        new_student = schema.load(incoming_data, session=db.session)

        
        db.session.add(new_student)
        db.session.commit()

  
        data = schema.dump(new_student)

        return jsonify(data), 201

    
    else:
        abort(409, "Student {sid}exists already".format(sid=sid))


def update(sid):
   
    incoming_data = request.get_json()

    update_person = Student.query.filter(
        Student.sid == sid
    ).one_or_none()

 
    if update_person is None:
        abort(
            404,
            "Person not found for Id: {sid}".format(sid=sid),
        )
   

    else:

       
        schema = StudentSchema()
        updateddata = schema.load(incoming_data, session=db.session)

       
        updateddata.sid = update_person.sid

        
        db.session.merge(updateddata)
        db.session.commit()

       
        data = schema.dump(updateddata)

        return jsonify(data), 200


def delete(sid):
  
    stud = Student.query.filter(Student.sid == sid).one_or_none()


    if stud is not None:
        db.session.delete(stud)
        db.session.commit()
        return {'message': 'Item deleted successfully'}, 200

    
    else:
        abort(
            404,
            "Student not found for Id: {sid}".format(sid=sid),
        )
