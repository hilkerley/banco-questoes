from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Disciplina, Questao, Prova
from .forms import AddQuestaoForm
from django.urls import reverse_lazy

class Disciplinas(LoginRequiredMixin, View):
    def get(self, request):
        disciplinas = Disciplina.objects.filter(professor = self.request.user).order_by('nome')
        return render(request, 'questoes/disciplinas.html', {'disciplinas': disciplinas})

    def post(self, request):
        disciplina = Disciplina(professor=self.request.user, nome=request.POST.get('nome'))
        disciplina.save()
        return redirect('questoes:disciplinas')

class DisciplinaDetalhes(View):
    def get(self, request, pk):
        questoes = Questao.objects.filter(disciplina = pk)
        disciplina = Disciplina.objects.filter(id = pk).first()
        return render(request, 'questoes/detalhes-disciplina.html', {'questoes': questoes, 'disciplina': disciplina})

    def post(self, request, pk):
        disciplina = Disciplina.objects.filter(id = pk).first()
        prova = Prova(professor=self.request.user, disciplina=disciplina, nome=request.POST.get('nome'))
        prova.save()
        return redirect('questoes:detalhes-disciplina', pk = pk)

class AddQuestao(CreateView):
    model = Questao
    template_name = 'questoes/add-questao.html'
    success_url = reverse_lazy('questoes:disciplinas')
    form_class = AddQuestaoForm

    def get_context_data(self, **kwargs):
        kwargs['disciplinas'] = Disciplina.objects.filter(professor = self.request.user).order_by('nome')
        return super(AddQuestao, self).get_context_data(**kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AddQuestao, self).form_valid(form)

class Questoes(View):
    def get(self, request):
        questoes = Questao.objects.filter(professor = self.request.user)
        return render(request, 'questoes/questoes.html', {'questoes': questoes})

class QuestaoDetalhes(View):
    def get(self, request, pk):
        provas = Prova.objects.filter(professor = self.request.user)
        questao = Questao.objects.filter(id = pk).first()
        return render(request, 'questoes/detalhes-questao.html', {'questao': questao, 'provas': provas})

    def post(self, request, pk):
        prova = Prova.objects.filter(id = request.POST.get('prova')).first()
        questao = Questao.objects.filter(id=pk).first()
        prova.questoes.add(questao)
        prova.save()
        return redirect('questoes:detalhes-questao', pk = pk)

class QuestaoExcluir(View):
    def get(self, request, pk):
        questao = Questao.objects.filter(id=pk).first()
        questao.delete()
        return redirect('questoes:disciplinas')

class QuestaoEditar(UpdateView):
    model = Questao
    template_name = 'questoes/update-questao.html'
    success_url = reverse_lazy('questoes:questoes')
    fields = ['enunciado', 'imagem', 'alternativa_um', 'alternativa_dois', 'alternativa_tres', 'alternativa_quatro', 'correta']

class Provas(View):
    def get(self, request):
        provas = Prova.objects.filter(professor = self.request.user)
        return render(request, 'questoes/provas.html', {'provas': provas})

class ProvaDetalhes(View):
    def get(self, request, pk):
        prova = Prova.objects.filter(id = pk).first()
        return render(request, 'questoes/detalhes-prova.html', {'prova': prova})