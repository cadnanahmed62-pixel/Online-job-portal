from django.db import models
from django.conf import settings
from jobs.models import Job


class JobApplication(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        ACCEPTED = 'ACCEPTED', 'Accepted'
        REJECTED = 'REJECTED', 'Rejected'

    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    cover_letter = models.TextField()
    cv = models.FileField(
        upload_to='cvs/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"


class Interview(models.Model):
    application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name='interviews'
    )
    interview_date = models.DateTimeField()
    meeting_link = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interview - {self.application.applicant.username}"