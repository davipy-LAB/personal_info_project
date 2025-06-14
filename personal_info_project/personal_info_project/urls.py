from django.contrib import admin
from django.urls import path
from info_app import views  # ⬅️ importa as views

# Aqui eu defino as URLs do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome, name='welcome'),
    path('goodbye/', views.goodbye, name='goodbye'),
    path('current-time/', views.current_time, name='current_time'),  # use hífen ou underline, só mantenha consistente
    path('greet/', views.greet, name='greet'),  # Rota para a nova view greet
    path('age/', views.age, name='age'),  # Rota para a nova view age
    path('sum/', views.calcular_sum, name='calcular_sum'),  # Rota para a nova view calcular_sum
]
# Note: Ensure that the 'info_app' is correctly named in your project structure.