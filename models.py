from heart import db
import uuid
from predict_model import scaler, model

class HeartAttack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    cp = db.Column(db.Float)
    trestbps = db.Column(db.Float)
    chol = db.Column(db.Float)
    fbs = db.Column(db.Float)
    restecg = db.Column(db.Float)
    thalach = db.Column(db.Float)
    exang = db.Column(db.Float)
    oldpeak = db.Column(db.Float)
    slope = db.Column(db.Float)
    ca = db.Column(db.Float)
    thal = db.Column(db.Float)
    result = db.Column(db.Integer)
    uuid = db.Column(db.String(36), unique=True)

    def __init__(self, **kwargs):
        self.uuid = str(uuid.uuid4())
        super(HeartAttack, self).__init__(**kwargs)
        self.set_result()

    def set_result(self):
        value_list = scaler.transform(
            [[self.age, self.sex, self.cp, self.trestbps, self.chol, self.fbs, self.restecg, self.thalach, self.exang,
              self.oldpeak, self.slope, self.ca, self.thal]])
        self.result = int(model.predict(value_list)[0])
