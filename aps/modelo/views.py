from django.shortcuts import render, redirect

from aps.modelo.models import User

from .forms import formularioUser


# Create your views here.
def principal(request):
	listado = User.objects.all().order_by('username')

	context = {

		'lista': listado,

	}

	return render (request, 'index.html', context)

def create_user(request):	

	formulario = formularioUser(request.POST)	

	if request.method == 'POST':
		
		if formulario.is_valid():

			datos = formulario.cleaned_data
			usuario = User()
			usuario.nombre = datos.get('nombre')
			usuario.username = datos.get('username')
			usuario.descripcion = datos.get('descripcion')
			usuario.fecha_nacimiento = datos.get('fecha_nacimiento')
			usuario.foto_perfil = "http://assets.stickpng.com/thumbs/585e4beacb11b227491c3399.png"
			usuario.celular = datos.get('celular')
			usuario.correo = datos.get('correo')
			usuario.password = datos.get('password')
			usuario.save()

			return redirect(principal)

	context = {
		'formulario': formulario,
	}
	
	return render (request, 'cliente/crear_usuario.html', context)


