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
def edit_project(request, project_id):
    user_role = get_user_role(request.user)
    project = get_object_or_404(Project, id=project_id, student=request.user)

    if project.status != 'pending':
        messages.error(request, 'Only pending projects can be edited.')
        return redirect('dashboard')

    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        messages.success(request, 'Project updated successfully.')
        return redirect('dashboard')

    return render(request, 'project_edit.html', {'form': form, 'project': project, 'user_role': user_role})

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, student=request.user)

    if project.status != 'pending':
        messages.error(request, 'Only pending projects can be deleted.')
        return redirect('dashboard')

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully.')
    return redirect('dashboard')

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
            project.save(update_fields=['status'])
            from .models import ProjectReview
            ProjectReview.objects.create(project=project, reviewed_by=request.user, status='approved', reason='Approved by teacher.')
            messages.success(request, f'Project "{project.title}" has been approved.')
        elif action == 'reject':
            rejection_reason = request.POST.get('rejection_reason', '').strip() or 'No rejection reason provided.'
            project.status = 'rejected'
            project.save(update_fields=['status'])
            from .models import ProjectReview
            ProjectReview.objects.create(project=project, reviewed_by=request.user, status='rejected', reason=rejection_reason)
            messages.success(request, f'Project "{project.title}" has been rejected.')

        return redirect('dashboard')

    latest_review = project.reviews.order_by('-reviewed_at').first()
    return render(request, 'project_review.html', {'project': project, 'user_role': user_role, 'latest_review': latest_review})