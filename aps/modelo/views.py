from django.shortcuts import render, redirect

from aps.modelo.models import User

from .forms import formularioUser

from django.contrib import messages


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
			usuario.foto_perfil = "static/photos/default.png"
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


