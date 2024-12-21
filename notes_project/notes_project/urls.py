"""
URL configuration for notes_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# notes_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes_app.urls')),
]

# notes_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('add/', views.add_note, name='add_note'),
    path('update/<int:pk>/', views.update_note, name='update_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
]