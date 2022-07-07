from django.contrib import admin
from .models import Ingredient, Recette, Categorie, Membre, Commentaire

# Register your models here.

admin.site.register(Categorie)
admin.site.register(Membre)
admin.site.register(Commentaire)

class IngredientInline(admin.TabularInline):
    model = Ingredient

@admin.register(Recette)

class RecipeAdmin(admin.ModelAdmin):
    inlines=[IngredientInline, ]
