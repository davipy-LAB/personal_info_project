from django.http import JsonResponse
from django.views import View
from datetime import datetime

class WelcomeView(View):
    def get(self, request):
        return JsonResponse({
            "message": "Hello there!",
            "author": "Made by: Davi Dias de Souza!"
        })

class CurrentTimeView(View):
    def get(self, request):
        now = datetime.now().strftime("%H:%M:%S")
        return JsonResponse({
            "current_time": now,
            "author": "Made by: Davi Dias de Souza!"
        })

class GreetView(View):
    def get(self, request):
        name = request.GET.get("name", "Stranger")
        return JsonResponse({
            "message": f"Hello, {name}!",
            "author": "Made by: Davi Dias de Souza!"
        })

class AgeView(View):
    def get(self, request):
        age = request.GET.get("age", "unknown")
        try:
            age = int(age)
        except ValueError:
            return JsonResponse({"error": "Invalid age", "author": "Made by: Davi Dias de Souza!"}, status=400)

        if age < 0:
            return JsonResponse({"error": "Age cannot be negative", "author": "Made by: Davi Dias de Souza!"}, status=400)
        elif age < 12:
            message = "You are a child!"
        elif age < 18:
            message = "You are a teenager!"
        elif age < 60:
            message = "You are an adult!"
        else:
            message = "You are a senior!"

        return JsonResponse({
            "message": message,
            "author": "Made by: Davi Dias de Souza!"
        })

class CalcularSumView(View):
    def get(self, request):
        try:
            a = int(request.GET.get("a", 0))
            b = int(request.GET.get("b", 0))
        except ValueError:
            return JsonResponse({"error": "Invalid parameters", "author": "Made by: Davi Dias de Souza!"}, status=400)
        
        if a < 0 or b < 0:
            return JsonResponse({"error": "Parameters must be non-negative integers", "author": "Made by: Davi Dias de Souza!"}, status=400)
        
        result = a + b
        return JsonResponse({
            "result": result,
            "author": "Made by: Davi Dias de Souza!"
        })
class GoodbyeView(View):
    def get(self, request):
        return JsonResponse({
            "message": "Goodbye!",
            "author": "Made by: Davi Dias de Souza!"
        })
    
from django.shortcuts import render
from datetime import datetime

def about_view(request):
    context = {
        'site_name': 'Informações Pessoais App',
        'site_description': 'Um site criado para demonstrar endpoints e lógica com Django.',
        'current_year': datetime.now().year
    }
    return render(request, 'about.html', context)

from django.http import JsonResponse
from .models import Person

def people_view(request):
    people = Person.objects.all()
    data = [
        {
            "id": person.id,
            "name": person.name,
            "age": person.age
        }
        for person in people
    ]
    return JsonResponse(data, safe=False)  # safe=False permite retornar listas

#------------------------------CÓDIGO NOVO--------------------------------#
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person
from .forms import PersonForm

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = reverse_lazy('people_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar nova Pessoa'
        return context

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = reverse_lazy('people_list')

#IMPORTAR O LISTVIEW PARA LISTAR AS PESSOAS
from django.views.generic import ListView

class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'
    context_object_name = 'people'

from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            satisfacao = form.cleaned_data['satisfacao']
            return render(request, 'agradecimento.html', {
                'nome': nome,
                'satisfacao': satisfacao
            })
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})

from django.shortcuts import render
from .models import Person

def filter_by_gender_view(request):
    gender = request.GET.get('gender')  # Ex: female
    people = Person.objects.all()
    if gender:
        people = people.filter(gender=gender)
    return render(request, 'people_filtered.html', {'people': people})


from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import ContactLog
from .forms import ContactLogForm

from django.views.generic.edit import CreateView
from .models import ContactLog



class ContactLogCreateView(CreateView):
    model = ContactLog
    form_class = ContactLogForm
    template_name = 'contactlog_form.html'
    success_url = '/contact-log/list/'


class ContactLogListView(ListView):
    model = ContactLog
    template_name = 'contactlog_list.html'
    context_object_name = 'logs'
