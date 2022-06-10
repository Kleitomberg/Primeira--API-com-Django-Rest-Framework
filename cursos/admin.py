from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao','atualizacao', 'ativo')

@admin.register(Avaliacao)
class AvaliacaiAdmin(admin.ModelAdmin):
    list_display = ('curso','nome','email','avaliacao','criacao','atualizacao', 'ativo')