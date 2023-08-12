# from django.http import HttpResponse

# def contact (request):
# return HttpResponse("It is  a contact page I developed in django")


from django.http import HttpResponse
from django.shortcuts import render


def mainHomepage(request):
    data = {
        'title': 'home page title',
        'pageName': "Home page",
        'courses': ["python", "php", "javascript", "dart", "C"],
        'count': [1, 2, 3, 4, 5, 6, 7, 8, 9, 23]
    }
    return render(request, "index.html", data)


def login(request):
    return render(request, 'login.html')


def register(request):
    try:
        email = request.GET['email']
        # another type to get method to get from data. here we use get function  
        password = request.GET.get("password") 
        Cpassword = request.GET['Cpassword']

        print(email)
        print(password, Cpassword)

    except:
        pass
    return render(request, 'register.html')


def home(request, courseID):
    return HttpResponse(courseID)


def aboutMe(request):
    return HttpResponse("Hi I am REJWAN AHAMED. it's my first django command running on server")
