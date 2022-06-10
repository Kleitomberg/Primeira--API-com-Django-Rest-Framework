
from pyexpat import model
from rest_framework import serializers

from .models import *

class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:

        extra_kwargs = {
            'email': {'write_only': True} #define que o campo email é visivel somente para escrita
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'url',            
            'criacao',
            'ativo',
            'atualizacao',
        ]

