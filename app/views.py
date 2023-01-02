from django.shortcuts import render

# Create your views here.
def looping(request):
    D={'name':'Arief'}
    return render(request,'looping.html',D)
    