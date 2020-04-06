from api import ma
from api.models import User


# Shemas
class UserShema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


# Init shemas
user_shema = UserShema()
users_shema = UserShema(many=True)
