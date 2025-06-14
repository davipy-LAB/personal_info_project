from django.http import JsonResponse
from datetime import datetime
# -*- coding: utf-8 -*-
#Aqui eu "seto" os defs
def welcome(request):
    return JsonResponse({
        "message": "Hello there!",
        "author": "Made by: Davi Dias de Souza!"
    })

def goodbye(request):
    return JsonResponse({
        "message": "Goodbye, see ya next time!",
        "author": "Made by: Davi Dias de Souza!"
    })

def current_time(request):
    now = datetime.now().strftime("%H:%M:%S")
    return JsonResponse({
        "current_time": now,
        "author": "Made by: Davi Dias de Souza!"
    })

def greet(request):
    if request.method != "GET":
        return JsonResponse({"error": "Only GET method is allowed!"}, status=405)
    name = request.GET.get("name", "Stranger")
    return JsonResponse({
        "message": f"Hello, {name}!",
        "author": "Made by: Davi Dias de Souza!"
    })

def age(request):
    if request.method != "GET":
        return JsonResponse({"error": "Only GET method is allowed!"}, status=405)
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

def calcular_sum(request):
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
