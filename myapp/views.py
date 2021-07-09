from django.shortcuts import render, redirect
from .models import People
from .forms import RecordForm, RecordUpdateForm
from django.http import JsonResponse


def home(request):
    
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

def add_record(request):
    # form = RecordForm()
    if request.method == 'POST':
        name = request.POST['name']
        birthday = request.POST['birthday']
        country = request.POST['country']
        organization = request.POST['organization']
        role = request.POST['role']

        p = People(name=name, birthday=birthday, country=country, organization=organization,role=role)
        p.save()