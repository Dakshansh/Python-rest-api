from shutil import copy

import pytest
import os
import connexion


def create_app(temp_db_file):
    basedir = os.path.abspath(os.path.dirname(__file__))

    connex_app = connexion.App(__name__, specification_dir=basedir)
    app = connex_app.app
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = temp_db_file
    connex_app.add_api("swaggert.yml")

    return app


@pytest.fixture(scope='function', autouse=True)
def client(tmpdir):
    # copy(f"D:/PythonScripts/API/Trial 7-3/student.db", tmpdir.dirpath())

    # temp_db_file = f"sqlite:///{tmpdir.dirpath()}"
    temp_db_file = f"sqlite:///D:/PythonScripts/API/Trial 7-3/student.db"
    app = create_app(temp_db_file)
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client
