from django.shortcuts import render
from .models import People

# Create your views here.
def home(request):
    template_name="myapp/home.html"
    people = People.objects.all()
    context={
        'people': people,
    }

    return render(request, template_name, context)