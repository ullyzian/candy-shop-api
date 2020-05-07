from sqlalchemy import event
from api import db
from api.models import TagItemRel


@event.listens_for(TagItemRel.__table__, "after_create")
def insert_debug(target, connection, **kwargs):
    db.session.add(TagItemRel(1, 1))
    db.session.add(TagItemRel(2, 1))
    db.session.add(TagItemRel(7, 1))

    db.session.add(TagItemRel(1, 2))
    db.session.add(TagItemRel(4, 2))

    db.session.add(TagItemRel(5, 3))
    db.session.add(TagItemRel(1, 3))

    db.session.add(TagItemRel(6, 4))

    db.session.commit()
