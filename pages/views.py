from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send confirmation email
        send_mail(
            subject="Contact Confirmation",
            message="Your message has been received successfully.",
            from_email="your_email@gmail.com",
            recipient_list=[email],
            fail_silently=False,
        )

        return redirect('home')

    return render(request, 'pages/contact.html')
