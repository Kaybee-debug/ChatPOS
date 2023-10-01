from django.shortcuts import render

# Create your views here.
def startup(request):
    return render(request,'business.html')
