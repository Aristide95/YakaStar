from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mission.models import Etudiant

def home(request):
    return render(request, 'example/home.html')


@login_required
def logged(request):
    '''context = {
        'user': request.user,
        'extra_data': request.user.social_auth.get(provider="epita").extra_data,
    }'''
    exist = Etudiant.objects.filter(email=request.user.email).exists()
    if exist == True:
        etudiant = Etudiant.objects.get(email=request.user.email)
    else:
        etudiant = Etudiant(firstname=request.user.first_name, lastname=request.user.last_name, email=request.user.email, status="ETUDIANT")
        etudiant.save()
    return render(request, 'example/logged.html', {'etudiant':etudiant})
