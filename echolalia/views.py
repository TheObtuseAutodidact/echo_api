from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Echo
# Create your views here.

def index(request):
    messages = Echo.objects.all()
    output = ', '.join([str(message) for message in messages])
    return HttpResponse(output)
    # return JsonResponse(output, safe=False)  just experimenting

def post(request, echo):
    shouted = { "echo: ": echo}
    Echo.objects.create(message=shouted['echo: '])
    return JsonResponse(shouted)


#
# def detail(request):
#     message = Echo.objects.last()
#     message = { "echo: ": str(message) }
#     return JsonResponse(message, safe=False)
