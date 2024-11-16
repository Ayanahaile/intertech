from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def name(request):
    return HttpResponse("Getu Haile")
def hobby(request):
    return JsonResponse({"hobby": "watching football"})
def dream(request):
    return HttpResponse("to be software engineer and business owner")