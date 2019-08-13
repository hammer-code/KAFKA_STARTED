from flask_restful import Resource, reqparse
from app.helpers.rest import response
from app import producer


class SendEmail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('messages', type=str, required=True)
        args = parser.parse_args()
        data = {
            "email": args['email'],
            "subject": "Test",
            "messages": args['messages']
        }
        try:
            producer.send("email_service", data)
        except Exception as e:
            return response(401, message=str(e))
        else:
            return response(200, data=data, message="Sending Email")