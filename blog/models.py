from cgi import test
from tkinter import Widget
from django.db import models
from django import forms

# Create your models here.

class Recette(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True)
    auteur= models.CharField(max_length=100)
    photo=models.CharField(max_length=250)
    date_parution=models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    categorie=models.ForeignKey('Categorie', on_delete=models.PROTECT, null=True)

    def __str__(self):

        return self.titre

class SubscribeForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=100)
    pseudo = forms.CharField(label='Pseudo', max_length=12)
    mdp = forms.CharField(label='Mdp', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')


class Membre(models.Model):
    nom = models.CharField(max_length=100)
    pseudo = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    mdp=models.CharField(max_length=20)
    dateInscription = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")

    def __str__(self):
        return self.nom


class Ingredient(models.Model):
    nom=models.CharField(max_length=100)
    quantite=models.IntegerField(max_length=11)
    unit=models.CharField(max_length=2)
    recette=models.ForeignKey('Recette', on_delete=models.PROTECT, related_name="ingredients", null=True)

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Commentaire(models.Model):
    auteur = models.CharField(max_length=100)
    contenu = models.TextField(max_length=1000)
    note = models.IntegerField(max_length=11)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name="Date de creation")
    arecette=models.ForeignKey('Recette', on_delete=models.PROTECT, related_name="arecette", null=True)

    def __str__(self):
        return self.auteur

class CommentForm(forms.Form):
    auteur = forms.CharField(max_length=100)
    contenu = forms.CharField(max_length=1000,widget=forms.Textarea)
    note = forms.IntegerField()

class LoginForm(forms.Form):
    pseudo = forms.CharField(max_length=100)
    mdp = forms.CharField(label='Mdp', widget=forms.PasswordInput)