from django import forms #importacion
from aps.modelo.models import User, Post, Comentario

class formularioUser(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:  
		model = User		
		fields = ["nombre", "username", "descripcion", "fecha_nacimiento",
				"celular", "correo"]
		widgets = {
            'password': forms.PasswordInput(),
        }

class formularioPost(forms.ModelForm):

	class Meta:
		model = Post
		fields = ["contenido", "descripcion", "etiquetas"]

class formularioComentario(forms.ModelForm):

	class Meta:
		model = Comentario
		fields = ["contenido"]

