from django.shortcuts import render, redirect
from .models import People
from .forms import RecordForm


def home(request):
    people = People.objects.all()
    if request.method == 'POST':
        form =  RecordForm(request.POST)  

        if form.is_valid():
            name = form.cleaned_data['name']
            birthday = form.cleaned_data['birthday']
            country = form.cleaned_data['country']
            organization = form.cleaned_data['organization']
            role = form.cleaned_data['role']

            p = People(name=name, birthday=birthday, country=country, organization=organization,role=role)
            p.save()

            return redirect('home')

    else:
        form = RecordForm()
    

    template_name="myapp/home.html"
    context={
        'form':form,
        'people':people,
    }
    return render(request, template_name,context)            

def delete_view(request,pk):
    p = People.objects.get(pk=pk)
    if request.method == 'POST':
        p.delete()
        return redirect('home')

    return render(request, template_name,context) 


    

