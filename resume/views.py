from django.shortcuts import render
from .models import Skill, Education, Achievement


def resume_view(request):
    skills = Skill.objects.all()
    education = Education.objects.all()
    achievements = Achievement.objects.all()

    return render(request, 'resume/resume.html', {
        'skills': skills,
        'education': education,
        'achievements': achievements
    })
