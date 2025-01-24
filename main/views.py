from django.shortcuts import render, redirect, get_object_or_404
from . models import Data
from . forms import DataForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    user = request.user
    data = Data.objects.filter(user=user)
    context = {
        'data':data
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def addData(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)  # Create the Data instance but don't save yet
            data.user = request.user        # Assign the logged-in user
            data.save()                     # Now save the instance to the database
            return redirect('home')         # Redirect to a success page (e.g., home)
    else:
        form = DataForm()

    context = {'form': form}
    return render(request, 'addData.html', context)

@login_required(login_url='login')
def details(request, id):
    data = Data.objects.get(id=id, user=request.user)
    context = {
        'data':data
    }
    return render(request, 'details.html', context)

@login_required(login_url='login')
def update(request, id):
    data = get_object_or_404(Data, id = id)
    if request.method == 'POST':
        form = DataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = DataForm(instance=data)
    
    context = {
        'form':form
    }

    return render(request, 'update.html', context)


def deleteData(request, pk):

    data = get_object_or_404(Data, pk=pk, user = request.user)

    data.delete()
 
    return redirect('home')