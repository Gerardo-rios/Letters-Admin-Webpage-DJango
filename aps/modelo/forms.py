from django import forms #importacion
from aps.modelo.models import User, Post, Comentario

class formularioUser(forms.ModelForm):

	class Meta:  
		model = User		
		fields = [
			"nombre",
			"correo",
			"celular",
			"password", 
			"username", 				
		]
		widgets= {
        "nombre": forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nombre del usuario', 'required': True, 'onfocus': 'this.placeholder = ""', 'onblur': 'this.placeholder = "Nombre del usuario"'}),
        "username": forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Username para el usuario', 'required': True, 'onfocus': 'this.placeholder = ""', 'onblur': 'this.placeholder = "Username para el usuario"'}),
        "celular": forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Número de celular del usuario', 'required': True, 'onfocus': 'this.placeholder = ""', 'onblur': 'this.placeholder = "Número de celular del usuario"', 'input type': 'number'}),
        "correo": forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'Correo electronico del usuario', 'required': True, 'onfocus': 'this.placeholder = ""', 'onblur': 'this.placeholder = "Correo electronico del usuario"'}),
        "password": forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Contraseña para el usuario', 'required': True, 'onfocus': 'this.placeholder = ""', 'onblur': 'this.placeholder = "Contraseña para el usuario"'})
        }


class formularioPost(forms.ModelForm):

	class Meta:
		model = Post
		fields = ["contenido"]

class formularioComentario(forms.ModelForm):

	class Meta:
		model = Comentario
		fields = ["contenido"]

class formularioLogin(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs = {'id': 'username', 'class':'login username-field', 'placeholder':'Username', 'required': True}))
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'id':'password', 'class':'login password-field', 'placeholder':'Password', 'required': True}))