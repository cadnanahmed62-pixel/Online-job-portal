
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobs.models import Job
from accounts.models import JobSeekerProfile
from .models import JobApplication, Interview
from django.utils import timezone
from django.utils.dateparse import parse_datetime


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, is_active=True)

    if request.user.role != 'JOB_SEEKER':
        messages.error(request, 'Only Job Seekers can apply for jobs.')
        return redirect('job_list')

    if JobApplication.objects.filter(
        applicant=request.user, job=job
    ).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('my_applications')

    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter', '').strip()
        cv = request.FILES.get('cv')

        if not cover_letter:
            messages.error(request, 'Please write your cover letter.')
        else:
            JobApplication.objects.create(
                applicant=request.user,
                job=job,
                cover_letter=cover_letter,
                cv=cv
            )
            messages.success(request, 'Your application was submitted successfully!')
            return redirect('my_applications')

    return render(request, 'applications/apply_job.html', {'job': job})


@login_required
def my_applications(request):
    applications = JobApplication.objects.filter(
        applicant=request.user
    ).order_by('-applied_at')

    return render(
        request,
        'applications/my_applications.html',
        {'applications': applications}
    )


@login_required
def employer_applications(request):
    if request.user.role != 'EMPLOYER':
        messages.error(request, 'Only Employers can view applications.')
        return redirect('home')

    applications = JobApplication.objects.filter(
        job__employer=request.user
    ).select_related('applicant', 'job').order_by('-applied_at')

    for application in applications:
        try:
            application.seeker_profile = application.applicant.job_seeker_profile
        except JobSeekerProfile.DoesNotExist:
            application.seeker_profile = None

    return render(
        request,
        'applications/employer_applications.html',
        {'applications': applications}
    )


@login_required
def update_application_status(request, application_id):
    if request.user.role != 'EMPLOYER':
        messages.error(request, 'Only Employers can update applications.')
        return redirect('home')

    application = get_object_or_404(
        JobApplication,
        id=application_id,
        job__employer=request.user
    )

    if request.method == 'POST':
        status = request.POST.get('status')

        if status in ['ACCEPTED', 'REJECTED']:
            application.status = status
            application.save()
            messages.success(request, 'Application status updated!')

    return redirect('employer_applications')


@login_required
def schedule_interview(request, application_id):
    if request.user.role != 'EMPLOYER':
        messages.error(request, 'Only Employers can schedule interviews.')
        return redirect('home')

    application = get_object_or_404(
        JobApplication,
        id=application_id,
        job__employer=request.user,
        status='ACCEPTED'
    )

    if request.method == 'POST':
        interview_date = parse_datetime(
            request.POST.get('interview_date', '')
        )
        meeting_link = request.POST.get('meeting_link', '')
        notes = request.POST.get('notes', '')

        if interview_date:
            if timezone.is_naive(interview_date):
                interview_date = timezone.make_aware(interview_date)

            Interview.objects.create(
                application=application,
                interview_date=interview_date,
                meeting_link=meeting_link,
                notes=notes
            )

            messages.success(request, 'Interview scheduled successfully!')
            return redirect('employer_applications')

        messages.error(request, 'Please enter a valid interview date.')

    return render(
        request,
        'applications/schedule_interview.html',
        {'application': application}
    )


@login_required
def my_interviews(request):
    if request.user.role != 'JOB_SEEKER':
        messages.error(request, 'Only Job Seekers can view interviews.')
        return redirect('home')

    interviews = Interview.objects.filter(
        application__applicant=request.user
    ).order_by('interview_date')

    return render(
        request,
        'applications/my_interviews.html',
        {'interviews': interviews}
    )
