from django.shortcuts import render

# Create your views here.
def index(reques):

    return render(reques, 'index.html')