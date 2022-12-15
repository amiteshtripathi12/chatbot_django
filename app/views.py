from django.shortcuts import render
from django.http import JsonResponse
import json
from .chat import  get_response

def index(request):
    return render(request, 'base.html', {})

def predict(request):
    text = request.get.json().get("message")
    #text = json.loads(request.message)
    response = get_response(text)
    message = {"answer":response}
    return JsonResponse(message)
