
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

    #incluir na lista de um obejto os objetos associados a ele
    
    #relação usando Nested relationships

         #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #relação usando Hyperlinked
  # avaliacoes = serializers.HyperlinkedRelatedField(
      #  many=True, read_only=True, view_name='avaliacao-detail'
  #  )

    
    #relação usando Primary key related fild
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'url',            
            'criacao',
            'ativo',
            'atualizacao',
            'avaliacoes',
        ]


  