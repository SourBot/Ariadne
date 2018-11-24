from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "A_Blog_App/index.html")

def build_post(request, blog_id):
    
