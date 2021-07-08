from django.shortcuts import render, redirect
from .models import People
from .forms import RecordForm, RecordUpdateForm
from django.http import JsonResponse


def home(request):
    
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

    return render(request)

# def update_view(request,pk):
#     people = People.objects.all()

#     p = People.objects.get(pk=pk)
    
#     if request.method == 'POST':
#         u_form = RecordUpdateForm(request.POST,instance=p)
#         if u_form.is_valid():
#             u_form.save()
#             return redirect('home')

#     else:
#         u_form = RecordUpdateForm(instance=p)
    
#     template_name="myapp/home.html"
#     context={
#         'people':people,
#         'u_form':u_form,
#     }
#     return render(request, template_name,context)

def update_view(request,pk):
    people = People.objects.all()

    p = People.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = RecordUpdateForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = RecordUpdateForm(instance=p)
    
    template_name="myapp/home.html"
    context={
        'people':people,
        'form':form,
    }
    return render(request, template_name,context)

def people(request):
    peoples = People.objects.all()
    
    data={
        'peoples':list(peoples.values()),
    }
    return JsonResponse(data)

