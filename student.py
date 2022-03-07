"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import abort, jsonify, request
from config import db
from models import Student, StudentSchema


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    stud = Student.query.all()

    # Serialize the data for the response
    student_schema = StudentSchema(many=True)
    data = student_schema.dump(stud)
    return jsonify(data)


def read_one(sid):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people

    :param sid:   Id of person to find
    :return:            person matching id
    """
    # Get the person requested
    stud = Student.query.filter(Student.sid == sid).one_or_none()

    # Did we find a person?
    if stud is not None:

        # Serialize the data for the response
        student_schema = StudentSchema()
        data = student_schema.dump(stud)
        return jsonify(data)

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            "Student not found for Id: {sid}".format(sid=sid),
        )


def create():
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param stude:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """

    incoming_data = request.get_json()
    sid = incoming_data['sid']
    existing_student = (
        Student.query.filter(Student.sid == sid).one_or_none()
    )

    # Can we insert this person?
    if existing_student is None:

        # Create a person instance using the schema and the passed in person
        schema = StudentSchema()
        new_student = schema.load(incoming_data, session=db.session)

        # Add the person to the database
        db.session.add(new_student)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(new_student)

        return jsonify(data), 201

    # Otherwise, nope, person exists already
    else:
        abort(409, "Student {sid}exists already".format(sid=sid))


def update(sid):
    """
    This function updates an existing person in the people structure
    Throws an error if a person with the name we want to update to
    already exists in the database.

    :param sid:   Id of the person to update in the people structure
    :param student:      person to update
    :return:            updated person structure
    """
    # Get the person requested from the db into session
    incoming_data = request.get_json()

    update_person = Student.query.filter(
        Student.sid == sid
    ).one_or_none()

    # Are we trying to find a person that does not exist?
    if update_person is None:
        abort(
            404,
            "Person not found for Id: {sid}".format(sid=sid),
        )
    # Otherwise, go ahead and update!

    else:

        # turn the passed in person into a db object
        schema = StudentSchema()
        updateddata = schema.load(incoming_data, session=db.session)

        # Set the id to the person we want to update
        updateddata.sid = update_person.sid

        # merge the new object into the old and commit it to the db
        db.session.merge(updateddata)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(updateddata)

        return jsonify(data), 200


def delete(sid):
    """
    This function deletes a person from the people structure

    :param sid:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    stud = Student.query.filter(Student.sid == sid).one_or_none()

    # Did we find a person?
    if stud is not None:
        db.session.delete(stud)
        db.session.commit()
        return {'message': 'Item deleted successfully'}, 200

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            "Student not found for Id: {sid}".format(sid=sid),
        )
