from sqlalchemy import event
from api import db
from api.models import User


@event.listens_for(User.__table__, "after_create")
def insert_users(target, connection, **kwargs):
    # Creating list of dictionaries (tags)
    users = [
        {
            "username": "admin",
            'email': "admin@domain.com",
            "password": "admin"
        },
        {
            "username": "user",
            'email': "user@domain.com",
            "password": "user"
        }
    ]

    # Adding items to Item table
    for user in users:
        instance = User(user["username"], user["email"])
        instance.set_password(user["password"])
        db.session.add(instance)

    db.session.commit()
