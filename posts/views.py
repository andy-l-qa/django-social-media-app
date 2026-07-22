from django.shortcuts import render

# Create your views here.
def home_view(request):
    # print('hello') # for debugging
    # print(request)
    # print(request.META)
    # print('Request method:', request.method)
    
    return render(request, 'posts/home.html')