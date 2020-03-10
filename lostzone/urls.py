"""lostzone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aps.modelo import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('log/', views.principal, name = 'prin'),
    path('', views.logear, name = 'logear'),
    path('home/', views.principal, name = 'home_reg'),
    path('unlog/', views.deslogear, name = 'unlog'),
    path('ban_cliente/', views.banearUser, name = 'desactivar_cliete'),
    path('unban_cliente/', views.unbanUser, name = 'activar_cliete'),
    path('posts/', views.publicaciones, name = 'publicaciones'),
    path('comen/', views.comentarios, name = 'comentarios'),
    path('delete_post/', views.deletearPost, name = 'borrar_publicacion'),
    path('delete_comen/', views.deletearComen, name = 'borrar_comentario'),
]
