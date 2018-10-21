from django.urls import path
from . import views as questoes

app_name = 'questoes'

urlpatterns = [
    path('', questoes.Disciplinas.as_view(), name='disciplinas'),
    path('disciplina/<pk>/detalhes', questoes.DisciplinaDetalhes.as_view(), name='detalhes-disciplina'),
    path('adicionar/questao', questoes.AddQuestao.as_view(), name='add-questao'),
    path('questoes/', questoes.Questoes.as_view(), name='questoes'),
    path('questao/<pk>/detalhes', questoes.QuestaoDetalhes.as_view(), name='detalhes-questao'),
    path('questao/<pk>/excluir', questoes.QuestaoExcluir.as_view(), name='excluir-questao'),
    path('questao/<pk>/editar', questoes.QuestaoEditar.as_view(), name='editar-questao'),
    path('provas/', questoes.Provas.as_view(), name='provas'),
    path('prova/<pk>/detalhes', questoes.ProvaDetalhes.as_view(), name='detalhes-prova'),
]