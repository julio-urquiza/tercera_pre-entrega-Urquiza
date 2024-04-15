from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.models import Alumno
from AppCoder.models import Profesor
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from AppCoder.forms import Alumno_formulario
from AppCoder.forms import Profesor_formulario

# Create your views here.

# def alta_curso(request,nombre):
#     curso = Curso(nombre=nombre, camada=232)
#     curso.save()
#     texto = f"se guardo en la bd el curso: {curso.nombre}{curso.camada}"
#     return HttpResponse(texto)

def inicio(request):
    return render(request, "padre.html")



def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    plantilla = loader.get_template("ver_cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos":alumnos}
    plantilla = loader.get_template("ver_alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores":profesores}
    plantilla = loader.get_template("ver_profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
    
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=request.POST["nombre"] , camada=request.POST["camada"])
            curso.save()

            return render(request , "formulario_curso.html")
    
    return render(request , "formulario_curso.html")

def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
    
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno( nombre=request.POST["nombre"] , legajo=request.POST["legajo"])
            alumno.save()

            return render(request , "formulario_alumno.html")
    
    return render(request , "formulario_alumno.html")

def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
    
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor( nombre=request.POST["nombre"] , legajo=request.POST["legajo"])
            profesor.save()

            return render(request , "formulario_profesor.html")
    return render(request , "formulario_profesor.html")




def buscar_curso(request):

    return render(request,"buscar_curso.html")

def buscar_alumno(request):

    return render(request,"buscar_alumno.html")

def buscar_profesor(request):

    return render(request,"buscar_profesor.html")



def buscar_resultado_curso(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render( request, "resultado_busqueda_curso.html",{"cursos":cursos})
    else:
        return HttpResponse("ingrese el nombre del curso")

def buscar_resultado_alumno(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        return render( request, "resultado_busqueda_alumno.html",{"alumnos":alumnos})
    else:
        return HttpResponse("ingrese el nombre del alumno")
    
def buscar_resultado_profesor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains=nombre)
        return render( request, "resultado_busqueda_profesor.html",{"profesores":profesores})
    else:
        return HttpResponse("ingrese el nombre del profesor")
