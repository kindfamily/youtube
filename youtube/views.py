from django.shortcuts import render
from .models import Cat

def cattube(request):
    cats = Cat.objects.all()
    
    return render(request, 'youtube/catlist.html', {
        'cats': cats,
})

