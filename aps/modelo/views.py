from django.shortcuts import render, redirect

from aps.modelo.models import User

from .forms import formularioUser, formularioLogin

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.urls import reverse

from django.contrib import messages

def logear(request):

	if request.method == 'POST':
		formulario = formularioLogin(request.POST)
		if formulario.is_valid():
			usuario = request.POST['username']
			clave = request.POST['password']
			user = authenticate(username = usuario, password = clave)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('home_reg'))
				else: 
					messages.add_message(request, messages.DANGER, "El usuario se encuentra desactivado")
			else: 
				messages.add_message(request, messages.WARNING, "Clave y / o Usuario Invalidos")
	else: 
		formulario = formularioLogin()
	context = {

		'form' : formulario,		

	}

	return render (request, 'login.html', context)

# Create your views here.
def principal(request):

	return render (request, 'otro.html')

def registrarse(request):	

	formulario = formularioUser(request.POST)	

	if request.method == 'POST':
		
		if formulario.is_valid():

			datos = formulario.cleaned_data
			usuario = User()
			usuario.nombre = datos.get('nombre')
			usuario.username = datos.get('username')
			#usuario.descripcion = "descripcion"
			usuario.fecha_nacimiento = datos.get('fecha_nacimiento')
			usuario.foto_perfil = "https://via.placeholder.com/150x150"
			#usuario.celular = "000000000"
			usuario.correo = datos.get('correo')
			usuario.password = datos.get('password')

			usuario.save()

			return redirect(principal)
		else:
			print("no es valido")
	else: 
		print("no es post")
		
	context = {
		'formulario': formulario,
	}
	
	return render (request, 'index.html', context)


