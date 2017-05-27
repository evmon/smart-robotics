from .models import Request


class SimpleMiddleware(object):

    def __init__(self, get_response):
    	
        self.get_response = get_response

        # one-time configuration and initialization

    def __call__(self, request):
        
        Request.objects.create(request=request)

        response = self.get_response(request)

        return response


