from django.shortcuts import render
from miapp.models import Course
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cursos(request):
    return render(request, 'cursos.html')

def crear_curso(request):
    return render(request, 'crear_curso.html')

def carreras(request):
    return render(request, 'carreras.html')

def crear_carrera(request):
    return render(request, 'crear_carrera.html')

def save_curso(request):
    if request.method == 'GET':
        code = request.GET['code']
        name = request.GET['name']
        hour = request.GET['hour']
        credits = request.GET['credits']
        state = request.GET['state']

    curso = Course(
        code = code,
        name = name,
        hour = hour,
        credits = credits,
        state = state
    )
    curso.save()
    courses = Course.objects.all()
    return render(request, 'cursos.html', {'courses': courses})

def cursos(request):
    courses = Course.objects.all()
    return render(request, 'cursos.html', {'courses': courses})