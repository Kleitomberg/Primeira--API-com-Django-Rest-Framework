from rest_framework import generics
from .models import *
from .serializers import *

from rest_framework.generics import get_object_or_404 

#Cria e lista Cursos

class CursosCreateAndListAPIView(generics.ListCreateAPIView):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()


#Cria e lista Avaliações
class AvaliacõesCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

   

#sobrescevendo metodos
    def get_queryset(self):
        if self.kwargs.get('curso_pk'): #verifica se  esta vindo um arfumento chamado curso apk
            id=self.kwargs.get('curso_pk')
            return self.queryset.filter(curso_id=id) #se sim, retornamos o queryseat com um filtro
        return self.queryset.all() #caso contrario retornamos todas as avalçiações

#Edita e deleta um curso
class CursoDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

#Edita e deleta uma avaliação
class AvaliacaoDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):

        if self.kwargs.get('curso_pk'):
            id_curso=self.kwargs.get('curso_pk')
            id_avaliacao=self.kwargs.get('avaliacao_pk')

            return get_object_or_404(self.get_queryset(),
            curso_id=id_curso,
            pk=id_avaliacao)

        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))