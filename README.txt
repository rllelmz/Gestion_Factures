PYTHON DJANGO 
Créer la base de données “database.sql” dans Phpmyadmin
Dans le terminal, aller dans le dossier de l’environnement virtuel avec cette commande : cd projectspython
L’activer : source bin/activate 
Création d’un projet django : Django-admin startproject nomprojet 
Aller dans le projet crée : cd nomprojet 
Activer le serveur : python manage.py runserver 
Faire les migrations : python manage.py migrate 
Se déconnecter du serveur : ctrl+c
Créer un superuser : python manage.py createsuper 
Se connecter à son compte en allant dans “http://127.0.0.1:8000/admin/“
Créer une application : python manage.py startapp nomapplication 
Ouvrir l’application dans Visual Studio Code via le terminal : code .
Dans “settings.py" du projet rajouter l’application crée dans “INSTALLED_APPS”
Créer dans le dossier de l’application : un dossier “templates”, 2 fichiers “forms.py” et “urls.py“
Dans “settings.py”, rajouter dans “DIRS” dans la partie “TEMPLATES” os.path.join(BASE_DIR, ‘chemin exact du templates’), et rajouter “import os” au dessus de “from pathlib import path”
Liaison avec la base de données MySql : aller dans “settings.py” et aller dans DATABASES et changer la base données de base “sqlite” avec MySql : DATABASES = { ‘default’ : { ’ENGINE’ : ‘django.db.backends.mysql’, ‘NAME’ : ‘Nom bdd’, ‘USER’ : ‘root’, ‘PASSWORD’ : ‘root’, ‘HOST’ : ‘127.0.0.1’, ‘PORT’ : ‘3306/8889’,}, ‘sqlite’: { ‘ENGINE’: django.db.backends.sqlite3, ‘NAME’ : BASE_DIR / ‘db.sqlite3’}}
Faire une migration : python manage.py migrate 
Re-activer le serveur : python manage.py runserver pr voir si il n’a pas d’erreur
Se déconnecter du serveur (ctrl+C) et faire : python manage.py createsuperuser puis entrer les informations demandées
Une fois la création du user, aller dans phpmyadmin puis dans la base de donnée entrée dans le “settings.py” et aller dans la table “auth_user” pour regarder si le nouveau user a bien été crée 
Une fois vérifié, faire : python manage.py inspectdb nomtable  → création automatique du modèle de la base de donnée (un modèle pour chaque table) dans le terminal
Coller copier le(s) modèle(s) dans “models.py” & changer si nécessaire car générer automatiquement 
 Faire python manage.py makemigrations puis python manage.py migrate 
Faire python manage.py runserver pour voir si le serveur n’a pas de problème 
Se déconnecter du serveur via “ctrl+c”
“admin.py” : from django.contrib import admin & from nomapplication.models import Nommodèle et dans le corps du code ajouter admin.site.register(Nommodel)
Dans “forms.py”, créer le formulaire “ModelForm” dans “models.py" : from django import forms & from nomapplication.models import Nomclassmodel puis définir class NomForm(form.ModelForm) : class meta : model = Nommodel fields = “__all__”
Créer les view : importer les bibliothèques nécessaires puis définir la view = nomdelavue(request) : form = NomForm() return render(request, ‘nomformàafficher.html’, {‘form’ : form}) (affiche toutes les données de la base)
Dans le dossier templates : créer le template nomform.html → pr simplifier la tâche mettre ! = code html et à l’intérieur du body mettre “{{ form }}” pour afficher le formulaire
Ajouter dans le “urls.py” de l’application : “from . import views” & “from django.urls import path”  puis urlpatterns = [ path(‘ ‘, views.nomdelavue)]
Ajouter dans le “urls.py” du projet : “from django.contrib import admin & from django.urls import include, path” urlpatterns = [ path(‘nom/ ‘, include(‘NomApplication.urls’), name=‘ajout’]
Activer le server : python manage.py runserver
Aller dans “http://127.0.0.1:8000/nom/" pour voir le formulaire créé
