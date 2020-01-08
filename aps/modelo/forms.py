from django import forms #importacion
from aps.modelo.models import User, Post, Comentario

class formularioUser(forms.ModelForm):

	class Meta:  
		model = User		
		fields = [
			"nombre",
			"correo",
			"password", 
			"fecha_nacimiento",
			"username", 				
		]
		widgets= {
        "nombre": forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Tu nombre', 'required': True, 'onfocus': 'this.placeholder = ""', 'onblur': 'this.placeholder = "Tu nombre"'}),
        "username": forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Tu nombre de usuario', 'required': True, 'onfocus': 'this.placeholder = ""', 'onblur': 'this.placeholder = "Tu nombre de usuario"'}),
        "fecha_nacimiento": forms.DateInput(format='%Y/%m/%d', attrs = {'class': 'form-control', 'placeholder': 'Fecha de nacimiento AA-MM-DD', 'required': True, 'onfocus': 'this.placeholder = ""', 'onblur': 'this.placeholder = "Fecha de nacimiento AA-MM-DD"'}),        
        "correo": forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'correo electronico', 'required': True, 'onfocus': 'this.placeholder = ""', 'onblur': 'this.placeholder = "correo electronico"'}),
        "password": forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'clave', 'required': True, 'onfocus': 'this.placeholder = ""', 'onblur': 'this.placeholder = "clave"'})
        }


class formularioPost(forms.ModelForm):

	class Meta:
		model = Post
		fields = ["contenido", "descripcion", "etiquetas"]

class formularioComentario(forms.ModelForm):

	class Meta:
		model = Comentario
		fields = ["contenido"]

class formularioLogin(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs = {'id': 'username', 'class':'login username-field', 'placeholder':'Username', 'required': True}))
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'id':'password', 'class':'login password-field', 'placeholder':'Password', 'required': True}))