
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job
from .forms import JobForm


def job_list(request):
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')

    search = request.GET.get('search', '').strip()
    location = request.GET.get('location', '').strip()
    category = request.GET.get('category', '').strip()

    if search:
        jobs = jobs.filter(title__icontains=search)

    if location:
        jobs = jobs.filter(location__icontains=location)

    if category:
        jobs = jobs.filter(category__name__icontains=category)

    return render(
        request,
        'jobs/job_list.html',
        {
            'jobs': jobs,
            'search': search,
            'location': location,
            'category': category,
        }
    )


def job_detail(request, job_id):
    job = get_object_or_404(
        Job,
        id=job_id,
        is_active=True
    )

    return render(
        request,
        'jobs/job_detail.html',
        {'job': job}
    )


@login_required
def post_job(request):
    if request.user.role != 'EMPLOYER':
        messages.error(request, 'Only employers can post jobs.')
        return redirect('home')

    if not request.user.is_employer_approved:
        messages.error(request, 'Your employer account is not approved.')
        return redirect('home')

    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()

            messages.success(request, 'Job posted successfully!')
            return redirect('job_list')
    else:
        form = JobForm()

    return render(request, 'jobs/post_job.html', {'form': form})


@login_required
def edit_job(request, job_id):
    if request.user.role != 'EMPLOYER':
        messages.error(request, 'Only employers can edit jobs.')
        return redirect('home')

    job = get_object_or_404(
        Job,
        id=job_id,
        employer=request.user
    )

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('job_list')
    else:
        form = JobForm(instance=job)

    return render(
        request,
        'jobs/edit_job.html',
        {'form': form, 'job': job}
    )


@login_required
def delete_job(request, job_id):
    if request.user.role != 'EMPLOYER':
        messages.error(request, 'Only employers can delete jobs.')
        return redirect('home')

    job = get_object_or_404(
        Job,
        id=job_id,
        employer=request.user
    )

    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('job_list')

    return render(
        request,
        'jobs/delete_job.html',
        {'job': job}
    )
