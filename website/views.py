from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def book(request):
    return render(request, 'website/book.html')

def contact(request):
    return render(request, 'website/contact.html')

