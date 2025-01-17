from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data = {
            'error': {
                'code': response.status_code,
                'message': response.data['detail'] if 'detail' in response.data else str(response.data)
            }
        }
    return response