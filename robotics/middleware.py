# from .models import PostRequest


# class SimpleMiddleware(object):

#     def __init__(self, get_response):
    	
#         self.get_response = get_response

#         # one-time configuration and initialization

#     def __call__(self, request):
        
#         info = 'Method: ' + str(request.method) + \
#         	   ', Full path: ' + str(request.get_full_path()) + \
#         	   ', HOST: '+ str(request.get_host())
               
#         if request.method == "POST":
#             PostRequest.objects.create(request=info)

#         response = self.get_response(request)
#         return response
