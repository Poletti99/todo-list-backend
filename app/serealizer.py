from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from models import Todo

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class TodoSchema(ma.ModelSchema):
    class Meta:
        model = Todo

    text = fields.Str(required=True)
    is_done = fields.Boolean(default=False)

    @validates("id")
    def validate_id(self, value):
        raise ValidationError("Não podemos receber o id na rota")
