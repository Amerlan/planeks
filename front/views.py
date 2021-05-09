from django.shortcuts import render, redirect


# Create your views here.

def create_schema(request):
    if request.user.is_authenticated:
        return render(request, 'create.html')
    return redirect('/login')


def login(request):
    return render(request, 'login.html')


def schemas(request):
    if request.user.is_authenticated:
        return render(request, 'table.html')
    return redirect('/login')
