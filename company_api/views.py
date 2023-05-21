from django.http import HttpResponse

def home_page(request):
    print("Home Page requested")
    friends=[
        'ankit',
        'r'
    ]
    return HttpResponse("This is Home page")