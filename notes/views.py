from django.shortcuts import render
from .models import Note

# Create your views here.
def index_view(request):

    notes = Note.objects.all()

    return render(request, "index.html", {"notes": notes})

def profile_view(request):

    name = "Reza"

    return render(request, "profile.html", {"name": name})