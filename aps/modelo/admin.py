from django.contrib import admin

# Register your models here.
from .models import User
from .models import Post
from .models import Comentario

class AdminUser(admin.ModelAdmin):

	list_display = ["nombre", "username", "descripcion", "foto_perfil"] 
	list_editable = ["descripcion"] 	
	search_fields = ["username", "nombre"]

	class Meta:
		model = User

admin.site.register(User, AdminUser)

class AdminPost(admin.ModelAdmin):

	list_display = ["contenido", "descripcion", "etiquetas", "created", "updated"]
	list_editable = ["descripcion"]	
	search_fields = ["etiquetas"]

	class Meta:
		model = Post

admin.site.register(Post, AdminPost)

class AdminComentario(admin.ModelAdmin):

	list_display = ["contenido", "created", "updated", "user", "post"]
	#list_editable = ["contenido"]		

	class Meta:
		model = Comentario

admin.site.register(Comentario, AdminComentario)