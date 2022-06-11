from rest_framework import generics
from .models import *
from .serializers import *

#Cria e lista Cursos

class CursosCreateAndListAPIView(generics.ListCreateAPIView):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()


#Cria e lista Avaliações
class AvaliacõesCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

#Edita e deleta um curso
class CursoDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

#Edita e deleta uma avaliação
class AvaliacaoDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer