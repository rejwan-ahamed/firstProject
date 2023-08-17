# from django.http import HttpResponse

# def contact (request):
# return HttpResponse("It is  a contact page I developed in django")


from django.http import HttpResponse, HttpResponseRedirect
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
    if request.method == "GET":
        result = request.GET.get('total')
    return render(request, 'login.html', {"output": result})


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


def postForm(request):
    print(request.POST)
    # if request.POST['password'] =="":
    #     return render(request, 'post.html', {"error": True})
    total = 0
    formData = {}
    try:
        number1 = int(request.POST['password'])
        number2 = int(request.POST.get("Cpassword"))
        total = number1 + number2

        formData = {
            "num1": number1,
            "num2": number2,
            "sum": total
        }

        url = "/login/?total={}".format(total)

        return HttpResponseRedirect(url)
    except:
        pass
    return render(request, 'post.html', formData)


def home(request, courseID):
    return HttpResponse(courseID)


def aboutMe(request):
    return HttpResponse("Hi I am REJWAN AHAMED. it's my first django command running on server")
