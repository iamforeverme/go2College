from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the login index.")


def profile(request):
    return HttpResponse("Hello, world. Here is your profile.")