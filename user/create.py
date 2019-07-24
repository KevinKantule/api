from flask_restful import Resource, request

from wtforms import Form, passwordField, validators, StringField

class NewUserForm(Form):
    phone = StringField('User Phone number', [validators.DataRequired()])
    password = passwordField('User password', [validators.DataRequired()])

class NewUser(Resource):
    def post(self):
        form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400
        return 'ok', 200
