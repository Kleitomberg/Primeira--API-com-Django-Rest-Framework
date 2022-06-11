from django.urls import path

from .views import *

urlpatterns = [
    path('cursos/', CursosCreateAndListAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacõesCreateAndListAPIView.as_view(), name='avaliacoes'),
    path('cursos/<int:pk>', CursoDeleteUpdateAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:pk>',AvaliacaoDeleteUpdateAPIView.as_view(), name='avaliacao')
]