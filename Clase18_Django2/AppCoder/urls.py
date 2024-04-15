from django.urls import path
from . import views

urlpatterns = [
    #path("alta_curso/<nombre>", views.alta_curso),
    path("",views.inicio, name="home"),

    path("ver_cursos",views.ver_cursos, name="cursos"),
    path("ver_alumnos",views.ver_alumnos, name="alumnos"),
    path("ver_profesores",views.ver_profesores, name="profesores"),

    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("alta_alumno", views.alumno_formulario, name="alta_alumno"),
    path("alta_profesor", views.profesor_formulario, name="alta_profesor"),

    path("buscar_curso", views.buscar_curso,name="buscar_curso"),
    path("buscar_alumno", views.buscar_alumno,name="buscar_alumno"),
    path("buscar_profesor", views.buscar_profesor,name="buscar_profesor"),

    path("buscar_resultado_curso",views.buscar_resultado_curso),
    path("buscar_resultado_alumno",views.buscar_resultado_alumno),
    path("buscar_resultado_profesor",views.buscar_resultado_profesor)

]