from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the home.")
def contact(request):
    return  HttpResponse("This is Contact Page")