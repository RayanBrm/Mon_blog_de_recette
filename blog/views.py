from cProfile import label
from multiprocessing import context
from attr import fields
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from .models import Categorie, CommentForm, LoginForm, Recette, Membre, SubscribeForm, Commentaire
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages


def index(request):
    
    p=None
    p_id= request.session.get('p_id')
    if(p_id):
        p=Membre.objects.get(pk=p_id)
    categories=Categorie.objects.all()
    recettes=Recette.objects.all()
    context={
        'recettes':recettes,
        'categories':categories,
        'p':p,
    }
    return render(request,'blog/accueil.html', context )

def categorie(request,idcategorie):
    recettes=Recette.objects.filter(categorie_id=idcategorie)
    categories=Categorie.objects.all()
    context={
        'recettes':recettes,
        'categories':categories,
        'idcategorie':idcategorie
    }
    return render(request,'blog/categorie.html',context)

def recette(request,idrecette):
    recette=Recette.objects.filter(pk=idrecette)
    commentaires=Commentaire.objects.filter(arecette=idrecette)
    arecette=Recette.objects.get(pk=idrecette)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            auteur = form.cleaned_data['auteur']
            contenu = form.cleaned_data['contenu']
            note=form.cleaned_data['note']
            p = Commentaire(auteur=auteur, contenu=contenu, note=note, arecette=arecette)
            p.save()
            messages.success(request, 'Form submission successful')
    else:
        form = CommentForm()

    context={
        'recette':recette,
        'commentaires':commentaires,
        'form':form,
    }

    return render(request, 'blog/recette.html', context)

def inscription(request):

    if request.method == 'POST':
        form_inscription = SubscribeForm(request.POST)
        if form_inscription.is_valid():
            nom = form_inscription.cleaned_data['nom']
            pseudo = form_inscription.cleaned_data['pseudo']
            mdp = form_inscription.cleaned_data['mdp']
            email=form_inscription.cleaned_data['email']
            p = Membre(nom=nom, pseudo=pseudo, mdp=make_password(mdp), email=email)
            p.save()
            messages.success(request, 'Form submission successful')
    else:
        form_inscription = SubscribeForm()
    
    return render(request, 'blog/inscription.html', {'form_inscription':form_inscription})

def logout(request):

    del request.session['p_id']

    return redirect('index')

def login(request):

    p=None
    form_login=LoginForm(request.POST)

    if request.method == 'POST':
        form_login = LoginForm(request.POST)
        if form_login.is_valid():
            pseudo=form_login.cleaned_data['pseudo']
            mdp=form_login.cleaned_data['mdp']
            try :
                p = Membre.objects.get(pseudo=pseudo)
            except ObjectDoesNotExist :
                messages.success(request, 'Votre nom d\'utilisateur ou votre mot de passe sont incorrect')
                return redirect('login')
            if check_password(mdp,p.mdp) :
                request.session['p_id']=p.id
                return redirect('index')
            else:
                messages.success(request, 'Votre nom d\'utilisateur ou votre mot de passe sont incorrect')
                return redirect('login')
        else:
            messages.success(request, 'Nous n\'avons pas réussi à vous connecter :(')
            form_login = LoginForm(request.POST)

    return render(request,'blog/login.html', {'form_login':form_login})
