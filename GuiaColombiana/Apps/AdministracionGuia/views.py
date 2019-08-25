import json

from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


from .models import Usuario
# Create your views here.


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        apellidoPaterno = jsonUser['apellidoPaterno']
        apellidoMaterno = jsonUser['apellidoMaterno']
        nombres = jsonUser['nombres']
        documento = jsonUser['documento']
        fechaNacimiento = jsonUser['fechaNacimiento']
        password = jsonUser['password']
        sexo = jsonUser['sexo']
        usuario = jsonUser['usuario']
        telefono = jsonUser['telefono']
        correo = jsonUser['correo']

        user_model = User.objects.create_user(usuario=usuario, password=password)
        user_model.nombres = nombres
        user_model.apellidoPaterno = apellidoPaterno
        user_model.apellidoMaterno = apellidoMaterno
        user_model.documento = documento
        user_model.fechaNacimiento = fechaNacimiento
        user_model.sexo = sexo
        user_model.telefono = telefono
        user_model.correo = correo
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))
