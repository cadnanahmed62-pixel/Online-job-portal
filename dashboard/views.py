
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from jobs.models import Job
from applications.models import JobApplication


@login_required
def home(request):
    return render(request, 'dashboard/home.html')


@login_required
def my_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.phone = request.POST.get('phone', '')
        profile.address = request.POST.get('address', '')
        profile.bio = request.POST.get('bio', '')
        profile.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('my_profile')

    return render(request, 'dashboard/my_profile.html', {'profile': profile})


@login_required
def reports(request):

    if request.user.role == 'EMPLOYER':
        jobs = Job.objects.filter(employer=request.user)

        applications = JobApplication.objects.filter(
            job__employer=request.user
        )

    else:
        jobs = Job.objects.none()

        applications = JobApplication.objects.filter(
            applicant=request.user
        )

    context = {
        'total_jobs': jobs.count(),
        'active_jobs': jobs.filter(is_active=True).count(),
        'total_applications': applications.count(),
        'pending_applications': applications.filter(status='PENDING').count(),
        'accepted_applications': applications.filter(status='ACCEPTED').count(),
        'rejected_applications': applications.filter(status='REJECTED').count(),
    }

    return render(request, 'dashboard/reports.html', context)
