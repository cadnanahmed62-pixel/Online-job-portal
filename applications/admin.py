from django.contrib import admin
from .models import JobApplication, Interview


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'applicant',
        'job',
        'status',
        'applied_at'
    )

    list_filter = ('status', 'applied_at')
    search_fields = ('applicant__username', 'job__title')


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = (
        'application',
        'interview_date',
        'meeting_link',
        'created_at'
    )

    list_filter = ('interview_date',)