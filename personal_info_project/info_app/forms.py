from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Digite sua idade'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return name

    def clean_age(self):
        age = self.cleaned_data['age']
        if age > 150:
            raise forms.ValidationError("A idade não pode ser maior que 150.")
        return age
    
from django import forms

class FeedbackForm(forms.Form):
    nome = forms.CharField(
        label="Nome",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'})
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'})
    )
    comentario = forms.CharField(
        label="Comentário",
        widget=forms.Textarea(attrs={'placeholder': 'Digite seu comentário'})
    )

    SATISFACAO_CHOICES = [
        ('Excelente', 'Excelente'),
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim'),
    ]
    satisfacao = forms.ChoiceField(label="Satisfação", choices=SATISFACAO_CHOICES)