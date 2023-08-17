# from django.http import HttpResponse

# def contact (request):
# return HttpResponse("It is  a contact page I developed in django")


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from firstProject.routes import router, Router


def mainHomepage(request):
    data = {
        'title': 'home page title',
        'pageName': "Home page",
        'courses': ["python", "php", "javascript", "dart", "C"],
        'count': [1, 2, 3, 4, 5, 6, 7, 8, 9, 23]
    }
    return render(request, "index.html", data)


def login(request):
    if request.method == "GET":
        result = request.GET.get('total')
    return render(request, 'login.html', {"output": result})


def register(request):
    try:
        email = request.GET['email']
        # another type to get method to get from data. here we use get function
        password = request.GET.get("password")
        c_password = request.GET['Cpassword']

        print(email)
        print(password, c_password)

    except:
        pass
    return render(request, 'register.html')


def postForm(request):
    context = {}
    if request.method == 'POST':
        password = request.POST.get('password', 'abc')
        confirm_password = request.POST.get("confirm_password", '')
        if password != confirm_password:
            context['error'] = "password doesn't match"
            context['password'] = password
            context['confirm_password'] = confirm_password
        else:
            return HttpResponseRedirect(router.Home)
    return render(request, 'post.html', context)


def home(request, courseID):
    return HttpResponse(courseID)


def aboutMe(request):
    return HttpResponse("Hi I am REJWAN AHAMED. it's my first django command running on server")
