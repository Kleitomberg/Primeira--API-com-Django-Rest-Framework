from django.urls import path



from .views import *

from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('cursos', CursoViewset)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosCreateAndListAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacĂµesCreateAndListAPIView.as_view(), name='avaliacoes'),
    path('cursos/<int:pk>', CursoDeleteUpdateAPIView.as_view(), name='curso'),
    path('avaliacoes/<avaliacao_pk>',AvaliacaoDeleteUpdateAPIView.as_view(), name='avaliacao'),

    path('cursos/<int:curso_pk>/avaliacoes', AvaliacĂµesCreateAndListAPIView.as_view(), name='curso-avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoDeleteUpdateAPIView.as_view(), name='avaliacaodecurso')

]