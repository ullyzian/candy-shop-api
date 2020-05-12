from sqlalchemy import event
from api import db
from api.models import TagItemRel


@event.listens_for(TagItemRel.__table__, "after_create")
def insert_debug(target, connection, **kwargs):
# Сhocolate
    db.session.add(TagItemRel(1, 1))
    db.session.add(TagItemRel(1, 2))
    db.session.add(TagItemRel(1, 4))
    db.session.add(TagItemRel(1, 5))
    db.session.add(TagItemRel(1, 6))
    db.session.add(TagItemRel(1, 7))
    db.session.add(TagItemRel(1, 8))
    db.session.add(TagItemRel(1, 9))
    db.session.add(TagItemRel(1, 10))
    db.session.add(TagItemRel(1, 11))
    db.session.add(TagItemRel(1, 12))
    db.session.add(TagItemRel(1, 13))
    db.session.add(TagItemRel(1, 14))
    db.session.add(TagItemRel(1, 16))

# Caramel
    db.session.add(TagItemRel(2, 1))
    db.session.add(TagItemRel(2, 4))
    db.session.add(TagItemRel(2, 9))
    db.session.add(TagItemRel(2, 16))

# Nougat
    db.session.add(TagItemRel(3, 5))
    db.session.add(TagItemRel(3, 1))

# Coconut
    db.session.add(TagItemRel(4, 6))
    db.session.add(TagItemRel(4, 16))

# Peanut
    db.session.add(TagItemRel(5, 3))
    db.session.add(TagItemRel(5, 16))

# Sour
    db.session.add(TagItemRel(6, 4))
    db.session.add(TagItemRel(6, 5))
    db.session.add(TagItemRel(6, 6))
    db.session.add(TagItemRel(6, 7))
# Lactose Free
    db.session.add(TagItemRel(7, 15))

# Present Box
    db.session.add(TagItemRel(8, 15))
    db.session.add(TagItemRel(8, 16))

# Waffles
    db.session.add(TagItemRel(9, 10))
    db.session.add(TagItemRel(9, 11))
    db.session.add(TagItemRel(9, 12))

# Marmalade
    db.session.add(TagItemRel(10, 15))
    db.session.add(TagItemRel(10, 16))

    db.session.commit()
