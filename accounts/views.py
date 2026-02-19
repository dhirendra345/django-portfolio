from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from projects.models import Project
from pages.models import Contact  # Change if your model name differs


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


def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
def dashboard(request):
    projects = Project.objects.order_by('-created_at')
    messages = Contact.objects.order_by('-created_at')

    context = {
        'projects': projects,
        'messages': messages,
    }

    return render(request, 'accounts/dashboard.html', context)
