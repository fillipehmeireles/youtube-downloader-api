from flask import jsonify


class Responses:
    def send(self, statusCode: int, message: str = '') -> map:
        return {
            "message": message,
            "statusCode":statusCode
        }