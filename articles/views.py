from django.shortcuts import render,HttpResponse

def articles(request):
    return HttpResponse("<h1>Hello World!</h1>")
def create_articles(request):
    return HttpResponse("<h1>Hello World2!</h1>")