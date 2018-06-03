from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mission.models import Etudiant, SocialAuthUsersocialauth
from django.db import connection
from pprint import pprint
from collections import namedtuple
import json
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


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
        etudiant = Etudiant(firstname=request.user.first_name, lastname=request.user.last_name, email=request.user.email, status="etudiant")
        etudiant.save()
    response = redirect('http://127.0.0.1:8080/#/', {'etudiant':etudiant})
    response.set_cookie('access_token', request.user.social_auth.get(provider="epita").extra_data['access_token'])
    return response

@csrf_exempt
def islogged(request):
    print(request.POST.get('access_token'))
    if request.POST.get('access_token') != None:
        tess = request.POST.get('access_token')
        test2 = '"access_token": "'+tess+'"'
        query = SocialAuthUsersocialauth.objects.filter(extra_data__icontains= test2)
        data = serializers.serialize('json', query)

        if data != []:
            kim = json.loads(data)
            return JsonResponse({"response" : True, "user_id": kim[0]['fields']['user_id']})
    else:
        return JsonResponse({"response" : False})


