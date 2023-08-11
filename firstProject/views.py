# from django.http import HttpResponse

# def contact (request):
#     return HttpResponse("It is  a contact page I developed in django")


from django.http import HttpResponse
from django.shortcuts import render


def mainHomepage(request):
    return render(request, "index.html")


def home(request, courseID):
    return HttpResponse(courseID)


def aboutMe(request):
    return HttpResponse("Hi I am REJWAN AHAMED. it's my first django command running on server")
