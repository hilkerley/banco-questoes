from django.db import models
from app.core.models import UUIDUser, CreateUpdateModel

class Disciplina(CreateUpdateModel):
    professor = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='professores', verbose_name='professor')
    nome = models.CharField(max_length=255, verbose_name='nome da disciplina')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'disciplina'
        verbose_name_plural = 'disciplinas'

class Questao(CreateUpdateModel):
    professor = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='teachers', verbose_name='professor')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='disciplinas', verbose_name='disciplina')
    enunciado = models.TextField(verbose_name='enunciado')
    imagem = models.ImageField(upload_to='images/', verbose_name='imagem da questão', blank=True)
    alternativa_um = models.CharField(max_length=255, verbose_name='1ª alternativa')
    alternativa_dois = models.CharField(max_length=255, verbose_name='2ª alternativa')
    alternativa_tres = models.CharField(max_length=255, verbose_name='3ª alternativa')
    alternativa_quatro = models.CharField(max_length=255, verbose_name='4ª alternativa')
    correta = models.CharField(max_length=255, verbose_name='alternativa correta')

    def __str__(self):
        return self.enunciado

    class Meta:
        verbose_name = 'questão'
        verbose_name_plural = 'questões'

class Prova(CreateUpdateModel):
    professor = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, verbose_name='professor', related_name='prof')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='disciplina', related_name='disciplina')
    nome = models.CharField(max_length=255, verbose_name='nome da prova')
    questoes = models.ManyToManyField(Questao, related_name='questions', verbose_name='questões da prova', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'prova'
        verbose_name_plural = 'provas'
