from flask import jsonify


def success_response(data):
    return jsonify(
        {
            'success': True,
            'data': data
        }
    ), 200


def bad_request():
    return jsonify(
        {
            'success': False,
            'message': 'Solicitud incorrecta'
        }
    ), 400
