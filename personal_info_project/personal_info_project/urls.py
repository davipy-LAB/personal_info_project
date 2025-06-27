from django.contrib import admin
from django.urls import path
from info_app import views  # Importando as views do arquivo views.py
from info_app.views import about_view  # Importando a view about_view do arquivo views.py
from info_app.views import people_view  # Importando a view people_view do arquivo views.py
from info_app.views import feedback_view  # Importando a view feedback_view do arquivo views.py

#Aqui eu estou importando as views do arquivo views.py que está na mesma pasta que o arquivo urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
    path('current-time/', views.CurrentTimeView.as_view(), name='current_time'),
    path('greet/', views.GreetView.as_view(), name='greet'),
    path('age/', views.AgeView.as_view(), name='age'),
    path('sum/', views.CalcularSumView.as_view(), name='calcular_sum'),
    path('goodbye/', views.GoodbyeView.as_view(), name='goodbye'),
    path('about/', about_view, name='about'),
    path('people/', people_view, name='people'),
    path('people/create/', views.PersonCreateView.as_view(), name='person_create'),
    path('people/update/<int:pk>/', views.PersonUpdateView.as_view(), name='person_update'),
    path('people/list/', views.PersonListView.as_view(), name='people_list'),
    path('feedback/', feedback_view, name='feedback'),
]
