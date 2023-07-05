from backend.methods import *
from backend.server import app

try:
    email = input("email:")
    password = input("password:")
    name = input("name:")
    clinic_id = input("name:")

    clinic = find_clinic_by_id(clinic_id)

    with app.app_context():
        create_user(email, password, name, clinic)

    print("ok!")
except ExplainableException as e:
    print(e.explain())