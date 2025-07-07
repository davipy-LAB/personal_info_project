from django.db import models

class Person(models.Model):
    GENDER_CHOICES = [
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('other', 'Outro'),
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='other')

    def __str__(self):
        return f"{self.name} ({self.age} anos)"
    
from django.db import models

# models.py
from django.db import models
from .models import Person

class ContactLog(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)