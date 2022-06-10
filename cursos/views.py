from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status


from .models import *
from .serializers import *



class CursoAPIView(APIView):   
    
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class AvaliacaoAPIView(APIView):
    
    '''
    API DO KABEH '''

    def get(self, request):
        print(request.user.id)        
        avaliacoes = Avaliacao.objects.all() 
        serializer = AvaliacaoSerializer(avaliacoes, many=True)        
        return Response(serializer.data)


    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data) #processo de deserializar, de JSON PARA PYTHON
        serializer.is_valid(raise_exception=True) #verifica se os dados são validos
        serializer.save() #salva no banco
        return Response(serializer.data, status=status.HTTP_201_CREATED) #Retorna resumo e satus
