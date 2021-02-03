from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ("Reminder Added to your List!"))
            return render(request, 'home.html', {'all_items': all_items})
    
    else:
        #pull objects from database
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    return render(request, 'about.html', {})

def delete(request, list_id):
    #instead of taking all we specify to take item where primary key = id
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Remainder has been Deleted!"))
    #redirect back to home
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ("Reminder Updated Successfully!"))
            return redirect('home')
    
    else:
        #pull objects from database
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})