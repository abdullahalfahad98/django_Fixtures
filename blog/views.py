from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def home(request):
    context={
        'posts': BlogPost.objects.all(),
        'total_posts': BlogPost.objects.count()
    }
    return render(request, 'home.html', context)
