from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest

def index(request):
    return HttpResponse("Hello world!")

def AgregarEdificios(request):
    return HttpResponse("Página Agregar Edificios")

########################################################################
#                       Vista Principal Sedes                         #
########################################################################
def sedes(request):
    if(request.method == "GET"):        
        try:
            return HttpResponse("Aquí va la vista principal de Sedes!")
        except:
            return HttpResponseBadRequest(["GET"], "Error en retorno de datos")
    else:        
        return HttpResponseNotAllowed(["GET"], "Método invalido")


