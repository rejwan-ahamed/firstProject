# from django.http import HttpResponse

# def contact (request):
#     return HttpResponse("It is  a contact page I developed in django")


from django.http import HttpResponse
from django.shortcuts import render


def mainHomepage(request):
    data = {
        'title': 'home page title',
        'pageName': "Home page",
        'courses': ["python", "php", "javascript", "dart", "C"],
    }
    return render(request, "index.html", data)


def home(request, courseID):
    return HttpResponse(courseID)


def aboutMe(request):
    return HttpResponse("Hi I am REJWAN AHAMED. it's my first django command running on server")
