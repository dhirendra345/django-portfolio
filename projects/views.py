from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/detail.html', {'project': project})
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'image', 'github_link', 'live_link']
    template_name = 'projects/form.html'
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['title', 'description', 'image', 'github_link', 'live_link']
    template_name = 'projects/form.html'
    success_url = reverse_lazy('projects')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('projects')
