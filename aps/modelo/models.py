from django.db import models

# Create your models here.
class User(models.Model):

	user_id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 100, null = False)
	username = models.CharField(max_length = 20, unique = True, null = False)
	descripcion = models.TextField(max_length = 120)
	foto_perfil = models.ImageField(upload_to='photos', default = None)
	celular = models.CharField(max_length = 10)
	status = models.BooleanField(default = True)
	correo = models.EmailField(max_length = 70, null = False, unique = True)
	password = models.CharField(max_length = 100, null = False)


class Post(models.Model):

	post_id = models.AutoField(primary_key = True)
	contenido = models.CharField(max_length = 280, null = False) 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(
		'User',
		null = False,
		on_delete = models.CASCADE,
	)

class Comentario(models.Model):

	coment_id = models.AutoField(primary_key = True)
	contenido = models.CharField(max_length = 80, null = False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
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
	seguidor = models.ForeignKey('User', null = False, related_name = 'seguidor', on_delete = models.CASCADE)
	seguido = models.ForeignKey('User', null = False, related_name = 'seguido', on_delete = models.CASCADE)

#class Notificaciones(models.Model):

	#noti_id = models.AutoField(primary_key = True)
	#contenido = models.CharField(max_length = 50)
	#user = models.ForeignKey(
	#		'User',
	#		null = False,
	#		on_delete = models.CASCADE
	#	)
	#post = models.ForeignKey(
	#		'Post',			
	#		on_delete = models.CASCADE
	#	) 

class Mensajes(models.Model):

	msj_id = models.AutoField(primary_key = True)
	mensaje = models.CharField(max_length = 100, null = False)
	receptor = models.ForeignKey('User', null = False, related_name = 'receptor', on_delete = models.CASCADE)
	sender = models.ForeignKey('User', null = False, related_name = 'sender', on_delete = models.CASCADE)

class Likes(models.Model):

	like_id = models.AutoField(primary_key = True)
	user_id = models.ForeignKey('User', null = False, on_delete = models.CASCADE)
	post_id = models.ForeignKey('Post', null = False, on_delete = models.CASCADE)