from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mission.models import UserLogin
from mission.serializers import UserLoginSerializer


@api_view(['GET','POST'])
def userLogin(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        userLogin = UserLogin.objects.all()
        serializer = UserLoginSerializer
        return Response(serializer.data)

    elif request.method == 'POST':
        userLogin = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
