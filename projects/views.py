from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm
from accounts.models import Profile

def get_user_role(user):
    try:
        profile = Profile.objects.get(user=user)
        return profile.role
    except Profile.DoesNotExist:
        return 'student'

def dashboard(request):
    if request.user.is_authenticated:
        user_role = get_user_role(request.user)
        if user_role == 'teacher':
            # Teacher sees all projects for review
            projects = Project.objects.all().order_by('-id')
            return render(request, 'teacher_dashboard.html', {'projects': projects, 'user_role': user_role})
        else:
            # Student sees only their own projects
            projects = Project.objects.filter(student=request.user).order_by('-id')
            return render(request, 'dashboard.html', {'projects': projects, 'user_role': user_role})
    else:
        return redirect('login')

@login_required
def add_project(request):
    user_role = get_user_role(request.user)
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.student = request.user
        project.save()
        messages.success(request, 'Project submitted successfully!')
        return redirect('dashboard')
    return render(request, 'project_add.html', {'form': form, 'user_role': user_role})

@login_required
def review_project(request, project_id):
    user_role = get_user_role(request.user)
    if user_role != 'teacher':
        messages.error(request, 'Access denied. Teachers only.')
        return redirect('dashboard')

    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            project.status = 'approved'
            messages.success(request, f'Project "{project.title}" has been approved.')
        elif action == 'reject':
            project.status = 'rejected'
            messages.success(request, f'Project "{project.title}" has been rejected.')
        project.save()
        return redirect('dashboard')

    return render(request, 'project_review.html', {'project': project, 'user_role': user_role})