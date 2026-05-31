from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, welcome to my Django app!")
    return render(request, 'index.html')
def about(request):
    return HttpResponse("Hello, welcome to about page of my Django app!")
def contact(request):
    return HttpResponse("Hello, welcome to contact page of my Django app!")