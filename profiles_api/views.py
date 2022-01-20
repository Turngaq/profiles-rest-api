from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    # Test API view

   def get(self, request, format=None):
        # Returns a list of API features
        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ] 
        something = "SOOOO"

        return Response({'message': 'Hello!', 'an_apiview': an_apiview, 'something': something})