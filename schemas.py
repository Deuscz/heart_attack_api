from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models import HeartAttack


class HeartAttackSchemaOutput(SQLAlchemySchema):
    class Meta:
        model = HeartAttack

    uuid = auto_field()
    result = auto_field()
    name = auto_field()

class HeartAttackSchema(SQLAlchemySchema):
    class Meta:`
        model = HeartAttack
        load_instance = True

    name = auto_field()
    age = auto_field()
    sex = auto_field()
    cp = auto_field()
    trestbps = auto_field()
    chol = auto_field()
    fbs = auto_field()
    restecg = auto_field()
    thalach = auto_field()
    exang = auto_field()
    oldpeak = auto_field()
    slope = auto_field()
    ca = auto_field()
    thal = auto_field()
