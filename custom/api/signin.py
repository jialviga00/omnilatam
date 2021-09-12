from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes((AllowAny,))
def api_signin(request):
    try:
        print()
        username = request.data['username']
        password = request.data['password']
    except:
        return Response(
                {'error': 'Please provide correct username and password'},
                status=HTTP_400_BAD_REQUEST
        )
    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'authenticated': True, 'token': "Token " + token.key})
    else:
        return Response(
            {'authenticated': False, 'token': None}, 
            status=HTTP_401_UNAUTHORIZED
        )
