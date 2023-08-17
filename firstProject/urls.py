from django.contrib import admin
from django.urls import path
from firstProject import views

urlpatterns = [
    path('', views.mainHomepage),
    path('login/', views.login, name="login"),
    path('register/', views.register),
    path('admin-panel/', admin.site.urls),
    path('post/', views.postForm),
    path('course/<courseID>',  views.home),
    path('course/', views.aboutMe),
]
