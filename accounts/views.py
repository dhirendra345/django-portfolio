from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from projects.models import Project

@login_required
def dashboard(request):
    projects = Project.objects.order_by('-created_at')
    return render(request, 'accounts/dashboard.html', {'projects': projects})
