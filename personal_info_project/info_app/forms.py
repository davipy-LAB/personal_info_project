from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'email', 'phone', 'gender']  # Incluindo todos os campos
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Digite sua idade'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Digite seu telefone'}),
            'gender': forms.Select(),
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
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email:
            raise forms.ValidationError("O e-mail deve conter um '@'.")
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit() or len(phone) < 10:
            raise forms.ValidationError("O telefone deve conter apenas números e ter pelo menos 10 dígitos.")
        return phone
    
    def clean_gender(self):
        gender = self.cleaned_data['gender']
        if gender not in ['male', 'female', 'other']:
            raise forms.ValidationError("O sexo deve ser 'male', 'female' ou 'other'.")
        return gender
    
    
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
