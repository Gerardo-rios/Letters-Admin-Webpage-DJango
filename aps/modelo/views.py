from django.shortcuts import render, redirect

from aps.modelo.models import User, Post

from .forms import formularioUser, formularioLogin

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.urls import reverse

from django.contrib import messages

#from django.contrib.auth.mixins import LoginRequiredMixin

host = "http://192.168.0.108:8080"

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
	if request.user.is_authenticated:
		return render (request, 'index.html')
	return render (request, 'login.html', context) 
	

# Create your views here.

def principal(request):
	#if usuario.groups.filter(name = 'Admin').exists():
	if request.user.is_authenticated:
		
		activos = User.objects.filter(status = 1)
		baneados = User.objects.filter(status = 0)

		context = {

		'lista': activos,
		'baneados': baneados,
		'host': host

		}

		return render (request, 'index.html', context)


	return redirect(logear) 

def publicaciones(request):

	if request.user.is_authenticated:
		
		posts = Post.objects.all().order_by('created_at')

		context = {

		'lista': posts,
		'host': host
		
		}

		return render (request, 'posts.html', context)

	return redirect(logear)
	

@login_required
def deslogear(request):

	logout(request)

	return redirect(logear)

def deletearPost(request):

	usuario = request.user

	if usuario.groups.filter(name = 'Admin').exists():

		external = request.GET['external']

		post = Post.objects.get(post_id = external)

		post.delete()

		return redirect(publicaciones)

	else: 
		messages.add_message(request, messages.ERROR, "No tienes autorizacion para hacer eso")
		return redirect(publicaciones)	


def banearUser(request):

	usuario = request.user


	if usuario.groups.filter(name = 'Admin').exists():

		external = request.GET['external']

		cliente = User.objects.get(user_id = external)
	
		cliente.status = False

		cliente.save()

		return redirect(principal)

	else: 
		messages.add_message(request, messages.ERROR, "No tienes autorizacion para hacer eso")
		return redirect(principal)	

def unbanUser(request):

	usuario = request.user

	if usuario.groups.filter(name = 'Admin').exists():

		external = request.GET['external']

		cliente = User.objects.get(user_id = external)
	
		cliente.status = True

		cliente.save()

		return redirect(principal)

	else: 
		messages.add_message(request, messages.ERROR, "No tienes autorizacion para hacer eso")
		return redirect(principal)	


#def registrarse(request):	

#	formulario = formularioUser(request.POST)	

#	if request.method == 'POST':
		
#		if formulario.is_valid():

#			datos = formulario.cleaned_data
#			usuario = User()
#			usuario.nombre = datos.get('nombre')
#			usuario.username = datos.get('username')
			#usuario.descripcion = "descripcion"
#			usuario.fecha_nacimiento = datos.get('fecha_nacimiento')
#    		usuario.foto_perfil = "https://via.placeholder.com/150x150"
			#usuario.celular = "000000000"
#			usuario.correo = datos.get('correo')
#			usuario.password = datos.get('password')

#			usuario.save()

#			return redirect(principal)
#		else:
#			print("no es valido")
#	else: 
#		print("no es post")
		
#	context = {
#		'formulario': formulario,
#	}
	
#	return render (request, 'REGISTROZONE.html', context)


