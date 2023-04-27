from django.shortcuts import render

# Create your views here.

def if_conditions(request):
    d={'a':200,'b':100,'c':500}

    return render(request,'if_conditions.html',d)

def looping_conditions(request):
    d={'CD':[1,2,3,4]}
    return render(request,'looping_conditions.html',d)