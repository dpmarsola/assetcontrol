from django.shortcuts import render
from django.http import HttpResponse
from app.transactions import initalInvestment


# Create your views here.
def index(request):
    
    try:
        result = initalInvestment("Jonh Doe", 1000)
    except ValueError as e:
        result = f"Error: {str(e)}"
        
    resp = HttpResponse()
    resp.write(result)
    resp.status_code = 200
    return  resp
