from django.db import models

# Create your models here.
class User(models.Model):

	user_id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 100, null = False)
	username = models.CharField(max_length = 20, unique = True, null = False)
	descripcion = models.TextField(max_length = 120)
	fecha_nacimiento = models.DateField(auto_now = False, auto_now_add = False, null = False)
	foto_perfil = models.ImageField(upload_to='photos', default = None)
	celular = models.CharField(max_length = 10)
	
	correo = models.EmailField(max_length = 70, null = False, unique = True)
	password = models.CharField(max_length = 100, null = False)

class Post(models.Model):

	post_id = models.AutoField(primary_key = True)
	contenido = models.FileField(upload_to='files', null = False)
	descripcion = models.TextField(max_length = 200) 
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	etiquetas = models.CharField(max_length = 200)
	user = models.ForeignKey(
		'User',
		null = False,
		on_delete = models.CASCADE,
	)

class Comentario(models.Model):

	coment_id = models.AutoField(primary_key = True)
	contenido = models.CharField(max_length = 200, null = False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(
			'User',
			null = False,
			on_delete = models.CASCADE
		)
	post = models.ForeignKey(
			'Post',
			null = False,
			on_delete = models.CASCADE
		) 

class Seguidores(models.Model):

	Seg_id = models.AutoField(primary_key = True)
	seguidor_id = models.ForeignKey('User', null = False, related_name = 'seguidor', on_delete = models.CASCADE)
	seguido_id = models.ForeignKey('User', null = False, related_name = 'seguido', on_delete = models.CASCADE)
	aceptado = models.BooleanField(default = True)

class Likes(models.Model):

	like_id = models.AutoField(primary_key = True)
	user = models.ForeignKey(
			'User',
			null = False,
			on_delete = models.CASCADE
		)
	post = models.ForeignKey(
			'Post',
			null = False,
			on_delete = models.CASCADE
		) 

class Notificaciones(models.Model):

	noti_id = models.AutoField(primary_key = True)
	contenido = models.CharField(max_length = 50)
	user = models.ForeignKey(
			'User',
			null = False,
			on_delete = models.CASCADE
		)
	post = models.ForeignKey(
			'Post',			
			on_delete = models.CASCADE
		) 
	