from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello, world. You're at the login index.")


@login_required
def profile(request):
    #if request.user.is_authenticated():
        # Do something for authenticated users.
    return HttpResponse("Hello, world. Here is your profile.")
