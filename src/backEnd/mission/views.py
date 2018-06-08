from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mission.models import UserLogin
from mission.serializers import UserLoginSerializer
from django.core.mail import EmailMessage

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

#p1, p2, p3 optional files
def sendmail(nom, email, society, phone, message, p1=None, p2=None, p3=None):
    body = 'Nom: '+ nom +'<br/>'
    body += 'Society: '+ society + '<br/>'
    body += 'Phone number: ' + str(phone) + '<br/><br/>'
    body += message
    
    email = EmailMessage(
    'Contact cristal',
    body,
    email,
    'levani.tevdoradze@epita.fr' #destinataire
    )
    
    if (p1 != None):
        email.attach_file(p1.name, p1.read(), p1.content_type())
        
    if (p2 != None):
        email.attach_file(p2.name, p2.read(), p2.content_type())
    
    if (p3 != None):
        email.attach_file(p3.name, p3.read(), p3.content_type())
        
    email.send()
