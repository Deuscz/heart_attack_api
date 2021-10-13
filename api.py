from flask_restful import Resource
from flask import request
from marshmallow.exceptions import ValidationError
from models import HeartAttack
from schemas import HeartAttackSchema, HeartAttackSchemaOutput
from heart import api, db, app

heart_attack_schema = HeartAttackSchema()
heart_attack_schema_output = HeartAttackSchemaOutput()
heart_attacks_schema_output = HeartAttackSchemaOutput(many=True)


class HeartAttacksApi(Resource):
    def post(self):
        json_data = request.json
        print(json_data)
        try:
            heart_attack = heart_attack_schema.load(data=json_data, session=db.session, partial=True)
        except ValidationError as e:
            return {"message": str(e)}, 422
        db.session.add(heart_attack)
        db.session.commit()
        return heart_attack_schema_output.dump(heart_attack)

    def get(self):
        messages = HeartAttack.query.order_by(HeartAttack.id.desc()).all()
        return heart_attacks_schema_output.dump(messages)


class HeartAttackApi(Resource):
    def get(self, heart_attack_uuid):
        heart_attack = HeartAttack.query.filter_by(uuid=heart_attack_uuid).first()
        if not heart_attack:
            return {"message": "Heart Attack predict not found"}, 404
        return heart_attack_schema_output.dump(heart_attack)

    def delete(self, heart_attack_uuid):
        affected_rows = HeartAttack.query.filter_by(uuid=heart_attack_uuid).delete()
        db.session.commit()
        if affected_rows == 0:
            return {"message": "Heart Attack predict not found"}, 404
        return "", 204

    def put(self, heart_attack_uuid):
        heart_attack = HeartAttack.query.filter_by(uuid=heart_attack_uuid).first()
        if not heart_attack:
            return {"message": "Heart Attack predict not found"}, 404
        heart_attack = heart_attack_schema.load(request.json, session=db.session, instance=heart_attack)
        db.session.add(heart_attack)
        db.session.commit()
        return heart_attack_schema_output.dump(heart_attack)


api.add_resource(HeartAttacksApi, '/heart_attack')
api.add_resource(HeartAttackApi, '/heart_attack/<heart_attack_uuid>')

# db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

