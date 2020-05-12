from sqlalchemy import event
from api import db
from api.models import Tag


@event.listens_for(Tag.__table__, "after_create")
def insert_tags(target, connection, **kwargs):
    # Creating list of dictionaries (tags)
    tags = [
        "Chocolate",
        "Caramel",
        "Nougat",
        "Coconut",
        "Peanut",
        "Sour",
        "Lactose free",
        "Present Box",
        "Waffles",
        "Marmalade"

    ]

    # Adding items to Item table
    for tag in tags:
        db.session.add(
            Tag(tag)
        )

    db.session.commit()
