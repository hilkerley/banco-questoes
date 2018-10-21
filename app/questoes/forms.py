from django import forms
from .models import Questao

class AddQuestaoForm(forms.ModelForm):
    def save(self, commit = True):
        file = super(AddQuestaoForm, self).save(commit=False)
        if commit:
            file.save()
        return file

    class Meta:
        model = Questao
        fields = ['professor', 'disciplina', 'enunciado', 'imagem', 'alternativa_um', 'alternativa_dois', 'alternativa_tres', 'alternativa_quatro', 'correta']
        labels = {
            'professor': 'Professor(a)',
            'disciplina': 'Disciplina',
            'enunciado': 'Enunciado',
            'imagem': 'Imagem (opcional)',
            'alternativa_um': '1ª Alternativa',
            'alternativa_dois': '2ª Alternativa',
            'alternativa_tres': '3ª Alternativa',
            'alternativa_quatro': '4ª Alternativa',
            'correta': 'Alternativa Correta',
        }
        widgets = {
            'imagem': forms.FileInput()
        }
