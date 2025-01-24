from django.shortcuts import render, redirect, get_object_or_404
from . models import Data
from . forms import DataForm

# Create your views here.

def home(request):
    data = Data.objects.all()
    context = {
        'data':data
    }
    return render(request, 'home.html', context)



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


def details(request, id):
    data = Data.objects.get(id=id, user=request.user)
    context = {
        'data':data
    }
    return render(request, 'details.html', context)


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